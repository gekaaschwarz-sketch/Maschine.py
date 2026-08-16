import sqlite3

print("\n============================================")
print("--- ⚙️ SQL-TABELLEN-UMBENENNUNG (RENAME) ---")
print("============================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Starte automatisierte Tabellen-Modernisierung...")

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alte_lkw_liste (
                id INTEGER PRIMARY KEY,
                kennzeichen TEXT
            );
        """)
        verbindung.commit()

        cursor.execute("ALTER TABLE alte_lkw_liste RENAME TO fuhrpark_fleet;")
        verbindung.commit()
        print("💎 SUCCESS: Tabelle erfolgreich in 'fuhrpark_fleet' umbenannt!")

    except sqlite3.OperationalError:
        print("⚠️ IGNORE: Die Modernisierung wurde bereits durchgeführt.")

print("\n⚙️ Umbenennungs-Modul abgeschlossen: Struktur erfolgreich modernisiert.")