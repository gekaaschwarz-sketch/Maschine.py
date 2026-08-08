import sqlite3
import os
import unittest

TEST_DB = "test_tresor.db"


class TestErrorHandling(unittest.TestCase):

    def setUp(self):
        """Läuft vor jedem Test - baut eine frische Test-DB mit UNIQUE-Schutz."""
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)
        verbindung = sqlite3.connect(TEST_DB)
        cursor = verbindung.cursor()
        cursor.execute("""
            CREATE TABLE kunden (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE
            )
        """)
        cursor.execute("INSERT INTO kunden (name) VALUES ('Hamburg-Kaffee AG')")
        verbindung.commit()
        verbindung.close()

    def test_abfrage_auf_nicht_existierende_tabelle_wirft_fehler(self):
        """Eine Abfrage auf eine Phantom-Tabelle muss OperationalError auslösen."""
        with sqlite3.connect(TEST_DB) as verbindung:
            cursor = verbindung.cursor()
            with self.assertRaises(sqlite3.OperationalError):
                cursor.execute("SELECT * FROM tabelle_die_es_nicht_gibt")

    def test_duplikat_wird_von_unique_index_blockiert(self):
        """Ein zweiter Kunde mit demselben Namen muss IntegrityError auslösen."""
        with sqlite3.connect(TEST_DB) as verbindung:
            cursor = verbindung.cursor()
            with self.assertRaises(sqlite3.IntegrityError):
                cursor.execute("INSERT INTO kunden (name) VALUES ('Hamburg-Kaffee AG')")

    def tearDown(self):
        """Läuft nach jedem Test - räumt die Test-DB wieder weg."""
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)


if __name__ == "__main__":
    unittest.main()