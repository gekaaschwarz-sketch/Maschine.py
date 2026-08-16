import sqlite3

print("\n=========================================")
print("--- 📝 SYSTEM-LOGBUCH (SQL-Tabelle) ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS system_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            zeitstempel DATETIME DEFAULT CURRENT_TIMESTAMP,
            aktion TEXT,
            status TEXT
        )
    """)
    verbindung.commit()

    aktions_text = "LKW-05 auf Route Hamburg-Zentrum geschickt"
    cursor.execute("INSERT INTO system_log (aktion, status) VALUES (?, ?)", (aktions_text, "ERFOLG"))
    verbindung.commit()

    cursor.execute("SELECT * FROM system_log")
    alle_logs = cursor.fetchall()

    print("\n📋️ Aktuelle Einträge im unbestechlichen System-Logbuch:")
    for eintrag in alle_logs:
        print(f"🕒️ [{eintrag[1]}] | 🛠️ {eintrag[2]} | Status: {eintrag[3]}")

print("\n⚙️ Logbuch-Modul abgeschlossen: Jede Sekunde lückenlos überwacht.")