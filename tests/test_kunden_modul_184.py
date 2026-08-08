import sqlite3
import os
import unittest
from kunden_modul_183 import kunde_hinzufuegen  # Import der eigenen Funktion!

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

    def test_neuer_kunde_wird_erfolgreich_hinzugefuegt(self):
        ergebnis = kunde_hinzufuegen(TEST_DB, "Alster-Logistik GmbH")
        self.assertTrue(ergebnis)

    def test_duplikat_wirft_verstaendlichen_valueerror(self):
        kunde_hinzufuegen(TEST_DB, "Hamburg-Kaffee AG")
        with self.assertRaises(ValueError):
            kunde_hinzufuegen(TEST_DB, "Hamburg-Kaffee AG")

    def tearDown(self):
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)


if __name__ == "__main__":
    unittest.main()