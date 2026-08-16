import sqlite3

print("\n=========================================")
print("--- ⚙️ SQL-TABELLEN-ERWEITERUNG (ALTER) ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Starte automatisierte Spalten-Erweiterung...")

    try:
        cursor.execute("""
            ALTER TABLE kunden
            ADD COLUMN telefonnummer TEXT DEFAULT 'KEINE NUMMER';
        """)
        verbindung.commit()
        print("💎 SUCCESS: Neue Spalte 'telefonnummer' erfolgreich angeschweißt!")

    except sqlite3.OperationalError:
        print("⚠️ IGNORE: Die Spalte 'telefonnummer' existiert bereits im Tresor.")

print("\n⚙️ Erweiterungs-Modul abgeschlossen: Tabellen-Struktur zukunftssicher angepasst.")