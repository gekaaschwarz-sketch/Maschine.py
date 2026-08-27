# name=tests/test_hauptprogramm_update.py
import os
import sqlite3
import unittest
import importlib.util
from pathlib import Path

TEST_DB = "test_hp099.db"


def load_module_from_path(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestHauptprogrammUpdate(unittest.TestCase):
    def setUp(self):
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)
        with sqlite3.connect(TEST_DB) as db:
            db.execute("""
                CREATE TABLE fleet_trucks (
                    id TEXT PRIMARY KEY,
                    fahrer_in TEXT,
                    last INTEGER,
                    extra_col INTEGER DEFAULT 12
                )
            """)
            db.execute("INSERT INTO fleet_trucks (id, fahrer_in, last) VALUES (?, ?, ?)",
                       ("A1", "Alice", 1000))
            db.commit()
        base = Path(__file__).resolve().parents[1]
        mod_path = base / "02_sqlite_basics" / "099_hauptprogramm_update.py"
        self.mod = load_module_from_path(mod_path, "hp099")

    def tearDown(self):
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)

    def test_update_missing_id_returns_false(self):
        result = self.mod.update_lkw_last(TEST_DB, "MISSING", 2000)
        self.assertFalse(result)
        with sqlite3.connect(TEST_DB) as db:
            row = db.execute("SELECT last FROM fleet_trucks WHERE id = 'A1'").fetchone()
            self.assertIsNotNone(row)
            self.assertEqual(row[0], 1000)

    def test_update_existing_id_returns_true_and_changes_value(self):
        result = self.mod.update_lkw_last(TEST_DB, "A1", 2500)
        self.assertTrue(result)
        with sqlite3.connect(TEST_DB) as db:
            row = db.execute("SELECT last FROM fleet_trucks WHERE id = 'A1'").fetchone()
            self.assertIsNotNone(row)
            self.assertEqual(row[0], 2500)


if __name__ == "__main__":
    unittest.main()