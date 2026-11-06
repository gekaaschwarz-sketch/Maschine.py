# Tests fuer Phase 2: 136_backup_check.py (nur temporaere Datenbanken)

import os
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.helpers import copy_script, create_test_db

LIVE = "speditions_tresor.db"
BACKUP = "speditions_tresor_BACKUP.db"
SCRIPT = "05_backup_restore/136_backup_check.py"


def run136(folder, *args, python_flags=()):
    """Startet die kopierte 136 im Ordner 'folder' mit Argumenten (helpers.py kann das nicht)."""
    name = copy_script(SCRIPT, folder)
    return subprocess.run(
        [sys.executable, *python_flags, name, *args],
        cwd=folder,
        text=True,
        capture_output=True,
    )


def create_full_db(path, rows=3):
    """Test-DB mit allen drei Pflichttabellen."""
    con = sqlite3.connect(str(path))
    con.execute("CREATE TABLE fleet_trucks (id TEXT, fahrer_in TEXT, last INTEGER)")
    con.execute("CREATE TABLE kunden (id INTEGER, name TEXT)")
    con.execute("CREATE TABLE system_log (id INTEGER, text TEXT)")
    for i in range(rows):
        con.execute("INSERT INTO fleet_trucks VALUES (?, ?, ?)", (f"HH-{i}", "Test", 1000 + i))
        con.execute("INSERT INTO kunden VALUES (?, ?)", (i, f"Kunde {i}"))
        con.execute("INSERT INTO system_log VALUES (?, ?)", (i, f"Eintrag {i}"))
    con.commit()
    con.close()


def folder_listing(folder):
    return sorted(os.listdir(folder))


class TestBackupCheckPhase2(unittest.TestCase):

    def test_ok_with_default_required_tables(self):
        with tempfile.TemporaryDirectory() as tmp:
            create_full_db(Path(tmp) / BACKUP)
            r = run136(tmp)
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            self.assertIn("SQL-INTEGRITY-OK", r.stdout)
            self.assertIn("Keine Aussage ueber Aktualitaet", r.stdout)
            self.assertNotIn("100%", r.stdout)

    def test_missing_file_exit_1_and_nothing_created(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = run136(tmp)
            self.assertEqual(r.returncode, 1, msg=r.stdout + r.stderr)
            self.assertEqual(folder_listing(tmp), ["136_backup_check.py"])

    def test_truncated_backup_exit_2(self):
        with tempfile.TemporaryDirectory() as tmp:
            backup = Path(tmp) / BACKUP
            create_full_db(backup, rows=3000)
            size = backup.stat().st_size
            with open(backup, "rb+") as f:
                f.truncate(size // 2)
            r = run136(tmp)
            self.assertEqual(r.returncode, 2, msg=r.stdout + r.stderr)

    def test_garbage_file_exit_2(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / BACKUP).write_bytes(b"das ist keine sqlite datenbank" * 200)
            r = run136(tmp)
            self.assertEqual(r.returncode, 2, msg=r.stdout + r.stderr)

    def test_zero_byte_file_exit_3(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / BACKUP).write_bytes(b"")
            r = run136(tmp)
            self.assertEqual(r.returncode, 3, msg=r.stdout + r.stderr)

    def test_missing_required_table_exit_3_names_table(self):
        with tempfile.TemporaryDirectory() as tmp:
            create_test_db(str(Path(tmp) / BACKUP))
            r = run136(tmp)
            self.assertEqual(r.returncode, 3, msg=r.stdout + r.stderr)
            self.assertIn("kunden", r.stdout)
            self.assertIn("system_log", r.stdout)

    def test_pflicht_option_replaces_required_list(self):
        with tempfile.TemporaryDirectory() as tmp:
            create_test_db(str(Path(tmp) / BACKUP))
            r = run136(tmp, "--pflicht", "fleet_trucks")
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            r = run136(tmp, "--pflicht=fleet_trucks")
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            r = run136(tmp, "--pflicht", "fleet_trucks,gibt_es_nicht")
            self.assertEqual(r.returncode, 3, msg=r.stdout + r.stderr)

    def test_usage_errors_exit_4(self):
        with tempfile.TemporaryDirectory() as tmp:
            create_test_db(str(Path(tmp) / BACKUP))
            for args in (
                ("--pflicht",),
                ("--pflicht", ","),
                ("--unbekannt",),
                ("a.db", "b.db"),
            ):
                r = run136(tmp, *args)
                self.assertEqual(r.returncode, 4, msg=str(args) + r.stdout + r.stderr)

    def test_path_argument_with_spaces(self):
        with tempfile.TemporaryDirectory() as tmp:
            sub = Path(tmp) / "ordner mit leerzeichen #1"
            sub.mkdir()
            create_full_db(sub / "vor_migration.db")
            r = run136(tmp, str(sub / "vor_migration.db"))
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)

    def test_zero_rows_in_required_table_is_only_a_hint(self):
        with tempfile.TemporaryDirectory() as tmp:
            create_full_db(Path(tmp) / BACKUP, rows=0)
            r = run136(tmp)
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            self.assertIn("0 Zeilen", r.stdout)

    def test_missing_optional_tables_is_only_a_hint(self):
        with tempfile.TemporaryDirectory() as tmp:
            create_full_db(Path(tmp) / BACKUP)
            r = run136(tmp)
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            self.assertIn("fuhrpark_fleet", r.stdout)

    def test_live_difference_is_only_a_hint_and_live_is_untouched(self):
        with tempfile.TemporaryDirectory() as tmp:
            create_full_db(Path(tmp) / BACKUP, rows=3)
            live = Path(tmp) / LIVE
            create_full_db(live, rows=5)
            live_before = live.read_bytes()
            r = run136(tmp)
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            self.assertIn("weichen von der Live-Datenbank ab", r.stdout)
            self.assertIn("Backup 3, Live 5", r.stdout)
            self.assertEqual(live.read_bytes(), live_before)

    def test_unreadable_live_db_is_only_a_hint(self):
        with tempfile.TemporaryDirectory() as tmp:
            create_full_db(Path(tmp) / BACKUP)
            (Path(tmp) / LIVE).write_bytes(b"kaputt" * 500)
            r = run136(tmp)
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            self.assertIn("nicht lesbar", r.stdout)

    def test_no_live_db_no_comparison(self):
        with tempfile.TemporaryDirectory() as tmp:
            create_full_db(Path(tmp) / BACKUP)
            r = run136(tmp)
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            self.assertNotIn("Live-Datenbank", r.stdout)

    def test_backup_file_is_not_modified(self):
        with tempfile.TemporaryDirectory() as tmp:
            backup = Path(tmp) / BACKUP
            create_full_db(backup)
            before = backup.read_bytes()
            listing_before = folder_listing(tmp)
            r = run136(tmp)
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            self.assertEqual(backup.read_bytes(), before)
            self.assertEqual(
                [n for n in folder_listing(tmp) if n != "136_backup_check.py"],
                listing_before,
            )

    def test_no_unclosed_database_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            create_full_db(Path(tmp) / BACKUP)
            create_full_db(Path(tmp) / LIVE)
            r = run136(tmp, python_flags=("-W", "error::ResourceWarning"))
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)
            self.assertNotIn("ResourceWarning", r.stderr)
            self.assertNotIn("unclosed", r.stderr)


if __name__ == "__main__":
    unittest.main()