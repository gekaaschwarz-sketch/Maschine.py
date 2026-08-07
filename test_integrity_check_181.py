import sqlite3
import os
import unittest

TEST_DB = "test_tresor.db"


class TestIntegrityCheck(unittest.TestCase):

    def setUp(self):
        """Läuft automatisch VOR jedem einzelnen Test."""
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)
        verbindung = sqlite3.connect(TEST_DB)
        cursor = verbindung.cursor()
        cursor.execute("CREATE TABLE test_tabelle (id INTEGER PRIMARY KEY, wert TEXT)")
        cursor.execute("INSERT INTO test_tabelle (wert) VALUES ('Hamburg')")
        verbindung.commit()
        verbindung.close()

    def test_intakte_datenbank_ist_ok(self):
        """Eine frisch erstellte, gesunde DB muss 'ok' melden."""
        with sqlite3.connect(TEST_DB) as verbindung:
            cursor = verbindung.cursor()
            cursor.execute("PRAGMA integrity_check;")
            ergebnis = cursor.fetchall()
            self.assertEqual(ergebnis[0][0], "ok")

    def test_tabelle_enthaelt_erwarteten_wert(self):
        """Prüft, ob die Testdaten korrekt gespeichert wurden."""
        with sqlite3.connect(TEST_DB) as verbindung:
            cursor = verbindung.cursor()
            cursor.execute("SELECT wert FROM test_tabelle WHERE id = 1")
            ergebnis = cursor.fetchone()
            self.assertEqual(ergebnis[0], "Hamburg")

    def tearDown(self):
        """Läuft automatisch NACH jedem Test - räumt auf."""
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)


if __name__ == "__main__":
    unittest.main()