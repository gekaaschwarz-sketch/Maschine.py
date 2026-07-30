import sqlite3

print("\n=====================================")
print("--- 🔬 AUTOMATISCHE INDEX-ZÄHLUNG ---")
print("=====================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Starte forensische Index-Zählung für die Tabelle 'kunden'...")
    try:
        cursor.execute("SELECT COUNT(*) FROM pragma_index_list('kunden');")
        anzahl_indizes = cursor.fetchone()[0]

        print(f"\n📊 Analyse-Bericht: Die Tabelle 'kunden' besitzt exakt {anzahl_indizes} aktiven Index/Indizes!")
        print("💎 SUCCESS: Index-Anzahl erfolgreich im laufenden Betrieb verifiziert.")

    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER BEI DER INDEX-ZÄHLUNG: {fehler}")

print("\n⚙️ Zähl-Modul abgeschlossen: Zweite Marathon-Etappe erfolgreich gemeistert.")