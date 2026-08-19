# Kernfunktionen fuer die Kundenverwaltung: Kunde anlegen (mit Duplikatschutz) und Kunde per Namen suchen
import sqlite3
from typing import Optional


class Kunde:
    """Repraesentiert einen einzelnen Kundendatensatz."""

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __repr__(self) -> str:
        return f"Kunde(id={self.id}, name='{self.name}')"


class KundenVerwaltung:
    """Kapselt alle Datenbank-Operationen rund um Kunden."""

    def __init__(self, db_pfad: str) -> None:
        self.db_pfad = db_pfad

    def hinzufuegen(self, name: str) -> bool:
        """
        Fuegt einen Kunden hinzu. Gibt True zurueck bei Erfolg.
        Wirft ValueError, wenn der Name bereits existiert.
        """
        with sqlite3.connect(self.db_pfad) as verbindung:
            cursor = verbindung.cursor()
            try:
                cursor.execute("INSERT INTO kunden (name) VALUES (?)", (name,))
                verbindung.commit()
                return True
            except sqlite3.IntegrityError:
                raise ValueError(f"Kunde '{name}' existiert bereits!")

    def suchen(self, name: str) -> Optional[Kunde]:
        """
        Sucht einen Kunden anhand des Namens.
        Gibt ein Kunde-Objekt zurueck, wenn gefunden.
        Gibt None zurueck, wenn kein Treffer existiert.
        """
        with sqlite3.connect(self.db_pfad) as verbindung:
            cursor = verbindung.cursor()
            cursor.execute("SELECT id, name FROM kunden WHERE name = ?", (name,))
            ergebnis = cursor.fetchone()
            if ergebnis is None:
                return None
            return Kunde(id=ergebnis[0], name=ergebnis[1])


if __name__ == "__main__":
    print("Dieses Modul stellt die Klassen Kunde und KundenVerwaltung bereit - fuer Nutzung im Hauptprogramm importieren.")