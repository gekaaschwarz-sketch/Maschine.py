import sqlite3

print("\n============================================")
print("--- 📸 AUTOMATISIERTER TABELLEN-SNAPSHOT ---")
print("============================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Starte krisensicheres Tabellen-Klonen (Snapshot)...")
    try:
        cursor.execute("DROP TABLE IF EXISTS lkw_flotte_backup_snapshot;")

        cursor.execute("""
            CREATE TABLE lkw_flotte_backup_snapshot AS
            SELECT * FROM lkw_flotte;
        """)
        verbindung.commit()
        print("💎 SUCCESS: Lokaler Sicherheits-Snapshot 'lkw_flotte_backup_snapshot' wurde erstellt!")

        cursor.execute("SELECT COUNT(*) FROM lkw_flotte_backup_snapshot;")
        zeilen_anzahl = cursor.fetchone()[0]
        print(f"📊 Integritäts-Prüfung: {zeilen_anzahl} LKW-Datensätze krisensicher gesichert.")

    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER BEIM SNAPSHOT-PROZESS: {fehler}")

print("\n⚙️ Snapshot-Modul abgeschlossen: Daten-Sicherheitsnetz erfolgreich gespannt.")