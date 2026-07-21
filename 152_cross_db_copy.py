import sqlite3

print("\n=========================================")
print("--- 📑 CROSS-DATABASE TABELLEN-KOPIE ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n📦️ Verbinde Live-Tresor mit der Archiv-Datenbank...")
    cursor.execute("ATTACH DATABASE 'speditions_archiv.db' AS archiv;")

    print("⚡️ Starte gezielten Tabellen-Import über Systemgrenzen hinweg...")
    try:
        cursor.execute("DROP TABLE IF EXISTS main.kunden_wiederhergestellt;")

        cursor.execute("""
            CREATE TABLE main.kunden_wiederhergestellt AS
            SELECT id, name, zugeordneter_lkw FROM archiv.system_log_historie;
        """)

        verbindung.commit()
        print("💎 SUCCESS: Tabelle erfolgreich über Datenbank-Grenzen hinweg kopiert!")

    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER BEIM CROSS-COPY: {fehler}")

print("\n⚙️ Kopier-Modul abgeschlossen: Datenrettung erfolgreich beendet.")