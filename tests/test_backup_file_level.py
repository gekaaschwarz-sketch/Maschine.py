import os
import sqlite3
import tempfile
import unittest
from pathlib import Path
from tests.helpers import copy_script, create_test_db, run_script_in_cwd, query_count

REPO_DB = "speditions_tresor.db"


class TestBackupFileLevel(unittest.TestCase):

    def test_backup_roundtrip(self):
        """129 -> 136 -> 145: create backup, verify integrity, restore and compare counts."""
        with tempfile.TemporaryDirectory() as tmp:
            dst_db = Path(tmp) / REPO_DB
            create_test_db(str(dst_db))

            s129 = copy_script('05_backup_restore/129_sql_backup.py', tmp)
            s136 = copy_script('05_backup_restore/136_backup_check.py', tmp)
            s145 = copy_script('05_backup_restore/145_sql_restore.py', tmp)

            r = run_script_in_cwd(s129, tmp)
            self.assertEqual(r.returncode, 0, msg=(r.stdout + r.stderr))
            backup_path = Path(tmp) / 'speditions_tresor_BACKUP.db'
            self.assertTrue(backup_path.exists())

            conn = sqlite3.connect(str(backup_path))
            cur = conn.cursor()
            cur.execute('PRAGMA integrity_check;')
            result = cur.fetchone()[0]
            conn.close()
            self.assertEqual(result, 'ok')

            orig_count = query_count(str(dst_db), 'fleet_trucks')

            r2 = run_script_in_cwd(s145, tmp)
            self.assertEqual(r2.returncode, 0, msg=(r2.stdout + r2.stderr))

            live_count = query_count(str(dst_db), 'fleet_trucks')
            self.assertEqual(live_count, orig_count)

    def test_backup_missing_handling(self):
        """When no backup exists, 136 and 145 must not destroy live DB and should handle gracefully."""
        with tempfile.TemporaryDirectory() as tmp:
            dst_db = Path(tmp) / REPO_DB
            create_test_db(str(dst_db))

            s136 = copy_script('05_backup_restore/136_backup_check.py', tmp)
            s145 = copy_script('05_backup_restore/145_sql_restore.py', tmp)

            backup_path = Path(tmp) / 'speditions_tresor_BACKUP.db'
            if backup_path.exists():
                backup_path.unlink()

            r = run_script_in_cwd(s136, tmp)
            self.assertEqual(r.returncode, 0, msg=(r.stdout + r.stderr))

            r2 = run_script_in_cwd(s145, tmp)
            self.assertEqual(r2.returncode, 0, msg=(r2.stdout + r2.stderr))
            self.assertTrue(dst_db.exists())

    def test_backup_rotation_keeps_maximum(self):
        """Ensure 178 keeps at most MAX_BACKUPS (3) and removes oldest files."""
        with tempfile.TemporaryDirectory() as tmp:
            dst_db = Path(tmp) / REPO_DB
            create_test_db(str(dst_db))

            backups_dir = Path(tmp) / 'backups'
            backups_dir.mkdir()
            names = [f'tresor_backup_2020010{i}_000000.db' for i in range(1, 6)]
            for name in names:
                (backups_dir / name).write_text('x')

            before = set(os.listdir(backups_dir))

            s178 = copy_script('05_backup_restore/178_backup_rotation.py', tmp)
            r = run_script_in_cwd(s178, tmp)
            self.assertEqual(r.returncode, 0, msg=(r.stdout + r.stderr))

            remaining = sorted([f for f in os.listdir(backups_dir) if f.startswith('tresor_backup_')])
            self.assertLessEqual(len(remaining), 3)
            after_set = set(remaining)
            new_files = after_set - before
            self.assertEqual(len(new_files), 1)
            all_files = sorted(list(before) + list(new_files))
            expected = all_files[-3:]
            self.assertEqual(remaining, expected)

    def test_corrupted_backup_detection_and_restore_behavior(self):
        """Create a corrupted backup and show that 136 detects corruption but 145 will still copy it (documented behavior)."""
        with tempfile.TemporaryDirectory() as tmp:
            dst_db = Path(tmp) / REPO_DB
            create_test_db(str(dst_db))

            s129 = copy_script('05_backup_restore/129_sql_backup.py', tmp)
            s136 = copy_script('05_backup_restore/136_backup_check.py', tmp)
            s145 = copy_script('05_backup_restore/145_sql_restore.py', tmp)

            r = run_script_in_cwd(s129, tmp)
            self.assertEqual(r.returncode, 0)
            backup_path = Path(tmp) / 'speditions_tresor_BACKUP.db'
            self.assertTrue(backup_path.exists())

            with open(backup_path, 'rb+') as f:
                f.seek(0, os.SEEK_END)
                size = f.tell()
                truncate_to = max(0, size - 100)
                f.truncate(truncate_to)

            conn = sqlite3.connect(str(backup_path))
            cur = conn.cursor()
            try:
                cur.execute('PRAGMA integrity_check;')
                res = cur.fetchone()
            except sqlite3.DatabaseError:
                res = (None,)
            conn.close()
            self.assertNotEqual(res, ('ok',))

            r2 = run_script_in_cwd(s145, tmp)
            self.assertEqual(r2.returncode, 0, msg=(r2.stdout + r2.stderr))

            conn2 = sqlite3.connect(str(dst_db))
            cur2 = conn2.cursor()
            try:
                cur2.execute('PRAGMA integrity_check;')
                live_res = cur2.fetchone()
            except sqlite3.DatabaseError:
                live_res = (None,)
            conn2.close()
            self.assertNotEqual(live_res, ('ok',))


if __name__ == '__main__':
    unittest.main()
