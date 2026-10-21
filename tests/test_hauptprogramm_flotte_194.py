# Tests fuer das Hauptprogramm 193_hauptprogramm_flotte.py

import contextlib
import importlib.util
import io
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


def load_module_from_path(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_main_with_inputs(module_path, inputs, db_path):
    mod = load_module_from_path(module_path, "hpflotte_testmod")
    stdout_buf = io.StringIO()
    with patch("builtins.input", side_effect=inputs):
        with contextlib.redirect_stdout(stdout_buf):
            ret = mod.main(db_pfad=db_path)
    return ret, stdout_buf.getvalue()


class TestHauptprogrammFlotte194(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.db_path = str(Path(self.tmpdir.name) / "test_flotte.db")
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE fleet_trucks ("
            "id TEXT, fahrer_in TEXT, last INTEGER, "
            "payload_tons INTEGER DEFAULT 12)"
        )
        cur.execute(
            "INSERT INTO fleet_trucks (id, fahrer_in, last) "
            "VALUES (?, ?, ?)",
            ("HH-01", "Erika", 2000),
        )
        cur.execute(
            "INSERT INTO fleet_trucks (id, fahrer_in, last) "
            "VALUES (?, ?, ?)",
            ("HH-02", "Maren", 3000),
        )
        conn.commit()
        conn.close()
        self.module_path = (
            Path(__file__).resolve().parents[1]
            / "193_hauptprogramm_flotte.py"
        )

    def tearDown(self):
        self.tmpdir.cleanup()

    def test_1_anzeige_shows_seed_rows(self):
        ret, out = run_main_with_inputs(
            self.module_path, ["1", "4"], self.db_path
        )
        self.assertIn(
            "ID: HH-01 | Fahrer_in: Erika | Last: 2000 kg", out
        )
        self.assertIn(
            "ID: HH-02 | Fahrer_in: Maren | Last: 3000 kg", out
        )
        self.assertEqual(ret, 0)

    def test_2_hinzufuegen_ok(self):
        ret, out = run_main_with_inputs(
            self.module_path,
            ["2", "TEST-01", "Tester", "1234", "4"],
            self.db_path,
        )
        self.assertIn("LKW TEST-01 erfolgreich hinzugefuegt.", out)
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT COUNT(*) FROM fleet_trucks WHERE id = ?",
                ("TEST-01",),
            ).fetchone()
        self.assertEqual(row[0], 1)
        self.assertEqual(ret, 0)

    def test_3_duplikat_shows_error_and_keeps_one(self):
        ret, out = run_main_with_inputs(
            self.module_path,
            ["2", "HH-01", "Erika", "2000", "4"],
            self.db_path,
        )
        self.assertIn(
            "Fehler: LKW mit id=HH-01 existiert bereits.", out
        )
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT COUNT(*) FROM fleet_trucks WHERE id = ?",
                ("HH-01",),
            ).fetchone()
        self.assertEqual(row[0], 1)
        self.assertEqual(ret, 0)

    def test_4_hinzufuegen_invalid_last(self):
        ret, out = run_main_with_inputs(
            self.module_path,
            ["2", "TEST-02", "Someone", "abc", "4"],
            self.db_path,
        )
        self.assertIn(
            "Ungueltige Zahl fuer Last. Vorgang abgebrochen.", out
        )
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT COUNT(*) FROM fleet_trucks WHERE id = ?",
                ("TEST-02",),
            ).fetchone()
        self.assertEqual(row[0], 0)
        self.assertEqual(ret, 0)

    def test_5_last_aktualisieren_ok(self):
        ret, out = run_main_with_inputs(
            self.module_path, ["5", "HH-01", "2500", "4"], self.db_path
        )
        self.assertIn(
            "LKW HH-01 erfolgreich auf 2500 kg gesetzt.", out
        )
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT last FROM fleet_trucks WHERE id = ?",
                ("HH-01",),
            ).fetchone()
        self.assertEqual(row[0], 2500)
        self.assertEqual(ret, 0)

    def test_6_last_unknown_id(self):
        ret, out = run_main_with_inputs(
            self.module_path, ["5", "NOPE", "4"], self.db_path
        )
        self.assertIn(
            "Kein LKW mit ID 'NOPE' gefunden. "
            "Kein Update durchgefuehrt.",
            out,
        )
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT last FROM fleet_trucks WHERE id = ?",
                ("HH-01",),
            ).fetchone()
        self.assertEqual(row[0], 2000)
        self.assertEqual(ret, 0)

    def test_7_last_abort_x(self):
        ret, out = run_main_with_inputs(
            self.module_path, ["5", "x", "4"], self.db_path
        )
        self.assertIn("Vorgang abgebrochen.", out)
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT last FROM fleet_trucks WHERE id = ?",
                ("HH-01",),
            ).fetchone()
        self.assertEqual(row[0], 2000)
        self.assertEqual(ret, 0)

    def test_8_loeschen_ok(self):
        ret, out = run_main_with_inputs(
            self.module_path, ["3", "HH-01", "4"], self.db_path
        )
        self.assertIn("LKW HH-01 erfolgreich geloescht.", out)
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT COUNT(*) FROM fleet_trucks WHERE id = ?",
                ("HH-01",),
            ).fetchone()
        self.assertEqual(row[0], 0)
        self.assertEqual(ret, 0)

    def test_9_loeschen_unknown_id(self):
        ret, out = run_main_with_inputs(
            self.module_path, ["3", "NOPE", "4"], self.db_path
        )
        self.assertIn(
            "Kein LKW mit ID 'NOPE' gefunden. Nichts geloescht.", out
        )
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT COUNT(*) FROM fleet_trucks WHERE id = ?",
                ("HH-01",),
            ).fetchone()
        self.assertEqual(row[0], 1)
        self.assertEqual(ret, 0)

    def test_10_loeschen_abort_x(self):
        ret, out = run_main_with_inputs(
            self.module_path, ["3", "x", "4"], self.db_path
        )
        self.assertIn("Loeschvorgang abgebrochen.", out)
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT COUNT(*) FROM fleet_trucks WHERE id = ?",
                ("HH-01",),
            ).fetchone()
        self.assertEqual(row[0], 1)
        self.assertEqual(ret, 0)

    def test_11_invalid_selection(self):
        ret, out = run_main_with_inputs(
            self.module_path, ["9", "4"], self.db_path
        )
        self.assertIn(
            "Ungueltige Auswahl. Bitte erneut versuchen.", out
        )
        self.assertEqual(ret, 0)

    def test_12_main_returns_0(self):
        ret, out = run_main_with_inputs(
            self.module_path, ["4"], self.db_path
        )
        self.assertIn("Auf Wiedersehen!", out)
        self.assertEqual(ret, 0)

    def test_13_leere_id_abbruch(self):
        with sqlite3.connect(self.db_path) as conn:
            before = conn.execute("SELECT COUNT(*) FROM fleet_trucks").fetchone()[0]

        ret, out = run_main_with_inputs(
            self.module_path,
            ["2", "", "4"],
            self.db_path,
        )
        self.assertIn("Ungueltige ID: darf nicht leer sein. Vorgang abgebrochen.", out)
        with sqlite3.connect(self.db_path) as conn:
            after = conn.execute("SELECT COUNT(*) FROM fleet_trucks").fetchone()[0]
        self.assertEqual(before, after)
        self.assertEqual(ret, 0)

    def test_14_id_nur_leerzeichen_abbruch(self):
        with sqlite3.connect(self.db_path) as conn:
            before = conn.execute("SELECT COUNT(*) FROM fleet_trucks").fetchone()[0]

        ret, out = run_main_with_inputs(
            self.module_path,
            ["2", "   ", "4"],
            self.db_path,
        )
        self.assertIn("Ungueltige ID: darf nicht leer sein. Vorgang abgebrochen.", out)
        with sqlite3.connect(self.db_path) as conn:
            after = conn.execute("SELECT COUNT(*) FROM fleet_trucks").fetchone()[0]
        self.assertEqual(before, after)
        self.assertEqual(ret, 0)

    def test_15_leere_fahrer_in_abbruch(self):
        ret, out = run_main_with_inputs(
            self.module_path,
            ["2", "TEST-03", "", "4"],
            self.db_path,
        )
        self.assertIn("Ungueltige Fahrer_in: darf nicht leer sein. Vorgang abgebrochen.", out)
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT COUNT(*) FROM fleet_trucks WHERE id = ?",
                ("TEST-03",),
            ).fetchone()
        self.assertEqual(row[0], 0)
        self.assertEqual(ret, 0)

    def test_16_negative_last_beim_hinzufuegen(self):
        ret, out = run_main_with_inputs(
            self.module_path,
            ["2", "TEST-04", "Tester", "-5", "4"],
            self.db_path,
        )
        self.assertIn("Ungueltige Last: darf nicht negativ sein. Vorgang abgebrochen.", out)
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT COUNT(*) FROM fleet_trucks WHERE id = ?",
                ("TEST-04",),
            ).fetchone()
        self.assertEqual(row[0], 0)
        self.assertEqual(ret, 0)

    def test_17_last_zero_erlaubt(self):
        ret, out = run_main_with_inputs(
            self.module_path,
            ["2", "TEST-05", "Tester", "0", "4"],
            self.db_path,
        )
        self.assertIn("LKW TEST-05 erfolgreich hinzugefuegt.", out)
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT COUNT(*) FROM fleet_trucks WHERE id = ?",
                ("TEST-05",),
            ).fetchone()
        self.assertEqual(row[0], 1)
        self.assertEqual(ret, 0)

    def test_18_negative_last_bei_update(self):
        ret, out = run_main_with_inputs(
            self.module_path,
            ["5", "HH-01", "-5", "4"],
            self.db_path,
        )
        self.assertIn("Ungueltige Last: darf nicht negativ sein. Vorgang abgebrochen.", out)
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT last FROM fleet_trucks WHERE id = ?",
                ("HH-01",),
            ).fetchone()
        self.assertEqual(row[0], 2000)
        self.assertEqual(ret, 0)


if __name__ == "__main__":
    unittest.main()
