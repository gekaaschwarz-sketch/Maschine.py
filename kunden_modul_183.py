import sqlite3


def kunde_hinzufuegen(db_pfad, name):
    """
    Fügt einen Kunden hinzu. Gibt True zurück bei Erfolg.
    Wirft ValueError, wenn der Name bereits existiert (statt rohem sqlite3-Fehler).
    """
    with sqlite3.connect(db_pfad) as verbindung:
        cursor = verbindung.cursor()
        try:
            cursor.execute("INSERT INTO kunden (name) VALUES (?)", (name,))
            verbindung.commit()
            return True
        except sqlite3.IntegrityError:
            raise ValueError(f"Kunde '{name}' existiert bereits!")


if __name__ == "__main__":
    print("Dieses Modul stellt kunde_hinzufuegen() bereit - für Nutzung im Hauptprogramm importieren.")