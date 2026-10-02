import os
import sqlite3
import tempfile
import unittest
from pathlib import Path
from tests.helpers import copy_script, create_test_db, run_script_in_cwd, query_count

REPO_DB = "speditions_tresor.db"


class TestTableSnapshot(unittest.TestCase):

    def test_snapshot_roundtrip(self):
        """163 snapshot -> simulate deletion -> 164 restore should repopulate fleet_trucks from snapshot."""
        with tempfile.TemporaryDirectory() as tmp:
            dst_db = Path(tmp) / REPO_DB
            create_test_db(str(dst_db))

            s163 = copy_script('05_backup_restore/163_table_snapshot.py', tmp)
            s164 = copy_script('05_backup_restore/164_data_restore.py', tmp)

            r = run_script_in_cwd(s163, tmp)
            self.assertEqual(r.returncode, 0, msg=(r.stdout + r.stderr))

            conn = sqlite3.connect(str(dst_db))
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM fleet_trucks_backup_snapshot;")
            snap_count = cur.fetchone()[0]

            cur.execute("DELETE FROM fleet_trucks;")
            conn.commit()

            cur.execute("SELECT COUNT(*) FROM fleet_trucks;")
            self.assertEqual(cur.fetchone()[0], 0)
            conn.close()

            r2 = run_script_in_cwd(s164, tmp)
            self.assertEqual(r2.returncode, 0, msg=(r2.stdout + r2.stderr))

            live_count = query_count(str(dst_db), 'fleet_trucks')
            self.assertEqual(live_count, snap_count)

    def test_snapshot_missing_abort(self):
        """If no snapshot exists, 164 should not delete live data and should abort gracefully."""
        with tempfile.TemporaryDirectory() as tmp:
            dst_db = Path(tmp) / REPO_DB
            create_test_db(str(dst_db))

            s164 = copy_script('05_backup_restore/164_data_restore.py', tmp)

            conn = sqlite3.connect(str(dst_db))
            cur = conn.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='fleet_trucks_backup_snapshot';")
            self.assertIsNone(cur.fetchone())
            conn.close()

            before = query_count(str(dst_db), 'fleet_trucks')

            r = run_script_in_cwd(s164, tmp)
            self.assertEqual(r.returncode, 0, msg=(r.stdout + r.stderr))

            after = query_count(str(dst_db), 'fleet_trucks')
            self.assertEqual(before, after)


if __name__ == '__main__':
    unittest.main()
