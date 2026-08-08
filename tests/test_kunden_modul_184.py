import sqlite3
import os
import unittest
from kunden_modul_183 import kunde_hinzufuegen, kunde_suchen  # Import der eigenen Funktionen!

TEST_DB = "test_tresor.db"


class TestKundenModul(unittest.TestCase):

    def setUp(self):
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)
        with sqlite3.connect(TEST_DB) as verbindung:
            verbindung.execute("""
                CREATE TABLE kunden (
                    id INTEGER PRIMARY KEY,
                    name TEXT UNIQUE
                )
            """)
        kunde_hinzufuegen(TEST_DB, "Hamburg-Kaffee AG")

    def test_neuer_kunde_wird_erfolgreich_hinzugefuegt(self):
        ergebnis = kunde_hinzufuegen(TEST_DB, "Alster-Logistik GmbH")
        self.assertTrue(ergebnis)

    def test_duplikat_wirft_verstaendlichen_valueerror(self):
        with self.assertRaises(ValueError):
            kunde_hinzufuegen(TEST_DB, "Hamburg-Kaffee AG")

    def test_vorhandener_kunde_wird_gefunden(self):
        ergebnis = kunde_suchen(TEST_DB, "Hamburg-Kaffee AG")
        self.assertIsNotNone(ergebnis)
        self.assertEqual(ergebnis[1], "Hamburg-Kaffee AG")

    def test_nicht_vorhandener_kunde_gibt_none_zurueck(self):
        ergebnis = kunde_suchen(TEST_DB, "Diesen-Kunden-gibt-es-nicht GmbH")
        self.assertIsNone(ergebnis)

    def tearDown(self):
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)


if __name__ == "__main__":
    unittest.main()
