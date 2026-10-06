# Tests fuer flotten_modul_191.py
# Test-DB: test_flotte.db (temporarisch im tmpdir)

import sqlite3
import tempfile
import unittest
from pathlib import Path

from flotten_modul_191 import FlottenVerwaltung, LKW

DB_NAME = "test_flotte.db"


class TestFlottenModul(unittest.TestCase):
    def setUp(self):
        """Erzeuge eine frische Test-DB (tempdir) mit fleet_trucks ohne Constraints."""
        self.tmpdir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.tmpdir.name) / DB_NAME
        conn = sqlite3.connect(str(self.db_path))
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE fleet_trucks (id TEXT, fahrer_in TEXT, last INTEGER, payload_tons INTEGER DEFAULT 12)"
        )
        # seed mit einer Beispielzeile
        cur.execute(
            "INSERT INTO fleet_trucks (id, fahrer_in, last) VALUES (?, ?, ?)",
            ("HH-01", "Erika", 2000),
        )
        conn.commit()
        conn.close()
        self.v = FlottenVerwaltung(str(self.db_path))

    def tearDown(self):
        try:
            self.tmpdir.cleanup()
        except Exception:
            pass

    def test_hinzufuegen_ok(self):
        result = self.v.hinzufuegen("HH-02", "Maren", 3000)
        self.assertTrue(result)
        conn = sqlite3.connect(str(self.db_path))
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM fleet_trucks WHERE id = ?", ("HH-02",))
        cnt = cur.fetchone()[0]
        conn.close()
        self.assertEqual(cnt, 1)

    def test_hinzufuegen_duplikat_raises_and_keeps_one(self):
        # bereits in setUp HH-01 vorhanden
        with self.assertRaises(ValueError):
            self.v.hinzufuegen("HH-01", "Erika", 2000)
        conn = sqlite3.connect(str(self.db_path))
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM fleet_trucks WHERE id = ?", ("HH-01",))
        cnt = cur.fetchone()[0]
        conn.close()
        self.assertEqual(cnt, 1)

    def test_suchen_found_and_none(self):
        l = self.v.suchen("HH-01")
        self.assertIsNotNone(l)
        self.assertIsInstance(l, LKW)
        self.assertEqual(l.id, "HH-01")
        self.assertEqual(l.fahrer_in, "Erika")
        self.assertEqual(l.last, 2000)
        none = self.v.suchen("HH-99")
        self.assertIsNone(none)

    def test_alle(self):
        self.v.hinzufuegen("HH-02", "Maren", 3000)
        alle = self.v.alle()
        self.assertIsInstance(alle, list)
        ids = sorted([o.id for o in alle])
        self.assertIn("HH-01", ids)
        self.assertIn("HH-02", ids)

    def test_loeschen_true_false(self):
        ok = self.v.loeschen("HH-01")
        self.assertTrue(ok)
        # nochmal loeschen -> False
        ok2 = self.v.loeschen("HH-01")
        self.assertFalse(ok2)

    def test_loeschen_unbekannte_id_laesst_vorhandene_zeile_unveraendert(self):
        # Loeschen einer unbekannten ID darf vorhandene Zeilen nicht veraendern
        res = self.v.loeschen("HH-99")
        self.assertFalse(res)
        conn = sqlite3.connect(str(self.db_path))
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*), fahrer_in, last FROM fleet_trucks WHERE id = ?", ("HH-01",))
        row = cur.fetchone()
        conn.close()
        # genau eine Zeile mit HH-01 und unveraenderten Werten
        self.assertIsNotNone(row)
        self.assertEqual(row[0], 1)
        self.assertEqual(row[1], "Erika")
        self.assertEqual(row[2], 2000)

    def test_last_aktualisieren_true_false(self):
        # existierend aktualisieren
        changed = self.v.last_aktualisieren("HH-01", 2500)
        self.assertTrue(changed)
        conn = sqlite3.connect(str(self.db_path))
        cur = conn.cursor()
        cur.execute("SELECT last FROM fleet_trucks WHERE id = ?", ("HH-01",))
        val = cur.fetchone()[0]
        conn.close()
        self.assertEqual(val, 2500)
        # nicht existierend: pruefe False und dass vorhandene Zeile unveraendert bleibt
        conn = sqlite3.connect(str(self.db_path))
        cur = conn.cursor()
        cur.execute("SELECT last FROM fleet_trucks WHERE id = ?", ("HH-01",))
        before = cur.fetchone()[0]
        conn.close()
        changed2 = self.v.last_aktualisieren("HH-99", 100)
        self.assertFalse(changed2)
        conn = sqlite3.connect(str(self.db_path))
        cur = conn.cursor()
        cur.execute("SELECT last FROM fleet_trucks WHERE id = ?", ("HH-01",))
        after = cur.fetchone()[0]
        conn.close()
        self.assertEqual(before, after)


if __name__ == "__main__":
    # Hinweis: Dieses Testmodul ist fuer die unittest-Discovery gedacht.
    # Starte mit: python3 -m unittest discover -s tests -p "*test*" -v
    import unittest
    unittest.main()