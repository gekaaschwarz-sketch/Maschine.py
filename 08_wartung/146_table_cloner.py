import sqlite3

print("\n=========================================")
print("--- 🔏 AUTOMATISCHER SQL-TABELLEN-KLON ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Erschaffe sterile Test-Umgebung (Sandbox)...")

    cursor.execute("DROP TABLE IF EXISTS kunden_sandbox;")
    cursor.execute("""
        CREATE TABLE kunden_sandbox (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            zugeordneter_lkw TEXT
        );
    """)

    print("📋️ Kopiere Live-Daten in die Test-Tabelle...")
    cursor.execute("""
        INSERT INTO kunden_sandbox (id, name, zugeordneter_lkw)
        SELECT id, name, zugeordneter_lkw FROM kunden;
    """)

    anzahl_geklont = cursor.rowcount
    verbindung.commit()

    print(f"\n💎 SUCCESS: {anzahl_geklont} Live-Einträge erfolgreich geklont!")
    print("🧪 Die Tabelle 'kunden_sandbox' steht bereit für Experimente.")

print("\n⚙️ Klon-Modul abgeschlossen: Entwicklungsumgebung sicher isoliert.")