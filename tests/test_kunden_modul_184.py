# Testet KundenVerwaltung: Kunde anlegen, Duplikat-Fehler, erfolgreiche Suche und Suche ohne Treffer
import sqlite3
import os
import unittest
from kunden_modul_183 import KundenVerwaltung

TEST_DB = "test_tresor.db"


class TestKundenVerwaltung(unittest.TestCase):

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
        self.verwaltung = KundenVerwaltung(TEST_DB)
        self.verwaltung.hinzufuegen("Hamburg-Kaffee AG")

    def test_neuer_kunde_wird_erfolgreich_hinzugefuegt(self):
        ergebnis = self.verwaltung.hinzufuegen("Alster-Logistik GmbH")
        self.assertTrue(ergebnis)

    def test_duplikat_wirft_verstaendlichen_valueerror(self):
        with self.assertRaises(ValueError):
            self.verwaltung.hinzufuegen("Hamburg-Kaffee AG")

    def test_vorhandener_kunde_wird_gefunden(self):
        kunde = self.verwaltung.suchen("Hamburg-Kaffee AG")
        self.assertIsNotNone(kunde)
        self.assertEqual(kunde.name, "Hamburg-Kaffee AG")

    def test_nicht_vorhandener_kunde_gibt_none_zurueck(self):
        kunde = self.verwaltung.suchen("Diesen-Kunden-gibt-es-nicht GmbH")
        self.assertIsNone(kunde)

    def tearDown(self):
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)


if __name__ == "__main__":
    unittest.main()