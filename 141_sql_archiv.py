import sqlite3

print("\n============================================")
print("--- 🗄️ AUTOMATISCHE TABELLEN-ARCHIVIERUNG ---")
print("============================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n📦️ Klinke Archiv-Datenbank in das System ein...")
    cursor.execute("ATTACH DATABASE 'speditions_archiv.db' AS archiv;")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS archiv.system_log_historie (
            id INTEGER PRIMARY KEY,
            zeitstempel DATETIME,
            aktion TEXT,
            status TEXT
        );
    """)

    print("⚡️ Starte Daten-Transfer in das Langzeit-Archiv...")
    cursor.execute("""
        INSERT INTO archiv.system_log_historie (id, zeitstempel, aktion, status)
        SELECT id, zeitstempel, aktion, status FROM main.system_log;
    """)

    anzahl_archiviert = cursor.rowcount

    cursor.execute("DELETE FROM main.system_log;")
    verbindung.commit()

    print(f"🗄️ SUCCESS: {anzahl_archiviert} historische Einträge sicher archiviert!")
    print("🧼 Der Live-Tresor wurde erfolgreich gesäubert und entlastet.")

print("\n⚙️ Archiv-Modul abgeschlossen: Daten-Infrastruktur zukunftssicher geschützt.")