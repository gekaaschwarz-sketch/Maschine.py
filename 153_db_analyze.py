import sqlite3

print("\n=========================================")
print("--- 📊 AUTOMATISCHE SQL-VOLLANALYSE ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Starte statistische Datenbank-Vollanalyse...")
    try:
        cursor.execute("ANALYZE;")
        verbindung.commit()
        print("💎 SUCCESS: Abfrage-Statistiken erfolgreich neu kalibriert!")

        cursor.execute("SELECT DISTINCT tbl FROM sqlite_stat1;")
        optimierte_tabellen = cursor.fetchall()

        print("\n📈 Optimierte Tabellen-Strukturen im Tresor:")
        for tabelle in optimierte_tabellen:
            print(f"✔️ Statistische Route berechnet für: {tabelle[0]}")

    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER BEI DER ANALYZE-PIPELINE: {fehler}")

print("\n⚙️ Analyse-Modul abgeschlossen: Triebwerke statistisch optimiert.")