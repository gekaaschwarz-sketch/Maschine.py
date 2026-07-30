import sqlite3

print("\n==============================================")
print("--- 🛡️ AUTOMATISCHER TABELLEN-SCAN-WÄCHTER ---")
print("==============================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Starte Sicherheits-Scan des Abfragepfads...")
    try:
        cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM lkw_flotte;")
        abfrage_plan = cursor.fetchall()

        scan_erkannt = False

        for schritt in abfrage_plan:
            erklaerung = schritt[3]
            if "SCAN" in erklaerung:
                scan_erkannt = True
                print(f"⚠️ WARNUNG: Unoptimierter Vollscan entdeckt -> {erklaerung}")

        if scan_erkannt:
            print("\n🚨 ALARM: Performance-Risiko! Tabelle wird ohne Index komplett durchsucht!")
        else:
            print("\n💎 SUCCESS: Abfrage-Pfad ist perfekt optimiert (Nutzt INDEX).")

    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER IM WÄCHTER-MODUL: {fehler}")

print("\n⚙️ Wächter-Modul abgeschlossen: Sicherheits-Check beendet.")