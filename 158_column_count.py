import sqlite3

print("\n=========================================")
print("--- 🔬 AUTOMATISCHE SPALTEN-ZÄHLUNG ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Starte forensische Spalten-Zählung für die Tabelle 'kunden'...")
    try:
        cursor.execute("SELECT COUNT(*) FROM pragma_table_info('kunden');")
        anzahl_spalten = cursor.fetchone()[0]

        print(f"\n📊 Analyse-Bericht: Die Tabelle 'kunden' besitzt exakt {anzahl_spalten} Spalten!")
        print("💎 SUCCESS: Spalten-Anzahl erfolgreich im laufenden Betrieb verifiziert.")

    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER BEI DER SPALTEN-ZÄHLUNG: {fehler}")

print("\n⚙️ Zähl-Modul abgeschlossen: Erste Marathon-Etappe erfolgreich gemeistert.")