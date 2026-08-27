import os
import sqlite3
import unittest
import importlib.util
from pathlib import Path

TEST_DB = "test_hp099_du_del.db"


def load_module_from_path(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestHauptprogrammDeleteUpdate(unittest.TestCase):
    def setUp(self):
        # Clean up old DB
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)

        # Create test DB with fleet_trucks table and one sample row
        with sqlite3.connect(TEST_DB) as db:
            db.execute("""
                CREATE TABLE fleet_trucks (
                    id TEXT PRIMARY KEY,
                    fahrer_in TEXT,
                    last INTEGER
                )
            """)
            db.execute("INSERT INTO fleet_trucks (id, fahrer_in, last) VALUES (?, ?, ?)",
                       ("A1", "Alice", 1000))
            db.commit()

        base = Path(__file__).resolve().parents[1]
        mod_path = base / "02_sqlite_basics" / "099_hauptprogramm_update.py"
        self.mod = load_module_from_path(mod_path, "hp099_du")

    def tearDown(self):
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)

    def test_lkw_existiert_true_false(self):
        self.assertTrue(self.mod.lkw_existiert(TEST_DB, "A1"))
        self.assertFalse(self.mod.lkw_existiert(TEST_DB, "NOPE"))

    def test_delete_missing_id_returns_false(self):
        # Deleting non-existing id returns False and does not affect existing row
        res = self.mod.delete_lkw(TEST_DB, "MISSING")
        self.assertFalse(res)
        with sqlite3.connect(TEST_DB) as db:
            row = db.execute("SELECT last FROM fleet_trucks WHERE id = 'A1'").fetchone()
            self.assertIsNotNone(row)
            self.assertEqual(row[0], 1000)

    def test_delete_existing_id_returns_true_and_removes_row(self):
        # Insert another row, then delete it
        with sqlite3.connect(TEST_DB) as db:
            db.execute("INSERT INTO fleet_trucks (id, fahrer_in, last) VALUES (?, ?, ?)",
                       ("B1", "Bob", 1500))
            db.commit()

        res = self.mod.delete_lkw(TEST_DB, "B1")
        self.assertTrue(res)

        with sqlite3.connect(TEST_DB) as db:
            row = db.execute("SELECT * FROM fleet_trucks WHERE id = 'B1'").fetchone()
            self.assertIsNone(row)


if __name__ == "__main__":
    unittest.main()