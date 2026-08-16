import sqlite3

print("\n==========================================")
print("--- ⚡️ AUTOMATISCHE LKW-INDEX-SCHMEIDE ---")
print("==========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n📦️ Starte Performance-Optimierung der LKW-Flotte...")
    try:
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_lkw_fahrer
            ON lkw_flotte (fahrer_in);
        """)
        verbindung.commit()
        print("💎 SUCCESS: Highspeed-Index 'idx_lkw_fahrer' erfolgreich gegossen!")

        print("\n🛡️ Wächter-Gegenprüfung: Durchleuchte neuen Abfragepfad...")
        cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM lkw_flotte WHERE fahrer_in = 'Valentin';")
        abfrage_plan = cursor.fetchall()

        for schritt in abfrage_plan:
            erklaerung = schritt[3]
            print(f"🔎 Neuer Weg-Marschplan: {erklaerung}")

    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER IN DER INDEX-SCHMIEDE: {fehler}")

print("\n⚙️ Optimierungs-Modul abgeschlossen: Triebwerke laufen im Highspeed-Modus.")