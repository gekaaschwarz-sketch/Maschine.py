import sqlite3

print("\n=========================================")
print("--- 🗑️ AUTOMATISCHE INDEX-VERNICHTUNG ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n📦️ Starte Bereinigung der Datenbank-Infrastruktur...")
    try:
        cursor.execute("DROP INDEX IF EXISTS idx_lkw_fahrer;")
        verbindung.commit()
        print("💎 SUCCESS: Index 'idx_lkw_fahrer' erfolgreich von der SSD gefegt!")

        print("\n🛡️ Wächter-Gegenprüfung: Durchleuchte den Abfragepfad...")
        cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM lkw_flotte WHERE fahrer_in = 'Valentin';")
        abfrage_plan = cursor.fetchall()

        for schritt in abfrage_plan:
            erklaerung = schritt[3]
            print(f"⚠️ Wächter-Bericht: {erklaerung}")

    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER BEI DER INDEX-VERNICHTUNG: {fehler}")

print("\n⚙️ Bereinigungs-Modul abgeschlossen: Infrastruktur erfolgreich entschlackt.")