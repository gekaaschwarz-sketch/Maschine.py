# Tests fuer Phase 1: 129_sql_backup.py (nur temporaere Datenbanken)

import os
import sqlite3
import tempfile
import unittest
from pathlib import Path

from tests.helpers import copy_script, create_test_db, run_script_in_cwd, query_count

LIVE = "speditions_tresor.db"
BACKUP = "speditions_tresor_BACKUP.db"
SCRIPT = "05_backup_restore/129_sql_backup.py"


def tmp_leftovers(folder):
    return [n for n in os.listdir(folder) if n.endswith(".tmp")]


class TestBackupPhase1(unittest.TestCase):

    def test_success_creates_valid_backup(self):
        with tempfile.TemporaryDirectory() as tmp:
            live = Path(tmp) / LIVE
            create_test_db(str(live))
            s = copy_script(SCRIPT, tmp)
            r = run_script_in_cwd(s, tmp)
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            backup = Path(tmp) / BACKUP
            self.assertTrue(backup.exists())
            con = sqlite3.connect(str(backup))
            self.assertEqual(con.execute("PRAGMA integrity_check").fetchall(), [("ok",)])
            con.close()
            self.assertEqual(query_count(str(backup), "fleet_trucks"),
                             query_count(str(live), "fleet_trucks"))
            self.assertEqual(tmp_leftovers(tmp), [])

    def test_missing_source_exit_1_and_old_backup_kept(self):
        with tempfile.TemporaryDirectory() as tmp:
            backup = Path(tmp) / BACKUP
            backup.write_bytes(b"alt")
            s = copy_script(SCRIPT, tmp)
            r = run_script_in_cwd(s, tmp)
            self.assertEqual(r.returncode, 1, msg=r.stdout + r.stderr)
            self.assertEqual(backup.read_bytes(), b"alt")
            self.assertEqual(tmp_leftovers(tmp), [])

    def test_missing_source_creates_no_backup(self):
        with tempfile.TemporaryDirectory() as tmp:
            s = copy_script(SCRIPT, tmp)
            r = run_script_in_cwd(s, tmp)
            self.assertEqual(r.returncode, 1)
            self.assertFalse((Path(tmp) / BACKUP).exists())

    def test_corrupt_source_exit_2_and_old_backup_kept(self):
        with tempfile.TemporaryDirectory() as tmp:
            live = Path(tmp) / LIVE
            live.write_bytes(b"das ist keine sqlite datenbank" * 100)
            backup = Path(tmp) / BACKUP
            backup.write_bytes(b"altes backup")
            s = copy_script(SCRIPT, tmp)
            r = run_script_in_cwd(s, tmp)
            self.assertEqual(r.returncode, 2, msg=r.stdout + r.stderr)
            self.assertEqual(backup.read_bytes(), b"altes backup")
            self.assertEqual(tmp_leftovers(tmp), [])

    def test_existing_backup_is_replaced_on_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            live = Path(tmp) / LIVE
            create_test_db(str(live))
            (Path(tmp) / BACKUP).write_bytes(b"alt")
            s = copy_script(SCRIPT, tmp)
            r = run_script_in_cwd(s, tmp)
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            self.assertEqual(query_count(str(Path(tmp) / BACKUP), "fleet_trucks"), 4)

    def test_source_is_not_modified(self):
        with tempfile.TemporaryDirectory() as tmp:
            live = Path(tmp) / LIVE
            create_test_db(str(live))
            before = live.read_bytes()
            s = copy_script(SCRIPT, tmp)
            r = run_script_in_cwd(s, tmp)
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            self.assertEqual(live.read_bytes(), before)

    def test_backup_contains_committed_data_of_wal_database(self):
        with tempfile.TemporaryDirectory() as tmp:
            live = Path(tmp) / LIVE
            create_test_db(str(live))
            con = sqlite3.connect(str(live))
            con.execute("PRAGMA journal_mode=WAL")
            con.execute("INSERT INTO fleet_trucks VALUES ('WAL-1', 'Test', 1, 12)")
            con.commit()
            s = copy_script(SCRIPT, tmp)
            r = run_script_in_cwd(s, tmp)
            con.close()
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            self.assertEqual(query_count(str(Path(tmp) / BACKUP), "fleet_trucks"), 5)

    def test_path_with_special_characters(self):
        with tempfile.TemporaryDirectory() as tmp:
            sub = Path(tmp) / "ordner mit leerzeichen #1"
            sub.mkdir()
            create_test_db(str(sub / LIVE))
            s = copy_script(SCRIPT, str(sub))
            r = run_script_in_cwd(s, str(sub))
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            self.assertTrue((sub / BACKUP).exists())


if __name__ == "__main__":
    unittest.main()