import sqlite3

print("\n============================================")
print("--- 🧬 AUTOMATISCHE TABELLEN-DNA-PRÜFUNG ---")
print("============================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Starte forensische Struktur-Analyse der Tabelle 'kunden'...")
    try:
        cursor.execute("PRAGMA table_info(lkw_flotte);")
        spalten_dna = cursor.fetchall()
        
        print("\n📋️ Offizieller DNA-Bericht der Tabellen_Struktur:")
        print(f"{'ID':<4} | {'Spaltenname':<20} | {'Datentyp':<10} | {'Pflichtfeld':<12} | {'PK':<4}")
        print("-" * 60)
        
        for spalte in spalten_dna:
            id_num = spalte[0]
            name = spalte[1]
            typ = spalte[2]
            pflicht = "JA" if spalte[3] == 1 else "NEIN"           
            pk = "JA" if spalte[5] == 1 else "NEIN"

            print(f"{id_num:<4} | {name:<20} | {typ:<10} | {pflicht:<12} | {pk:<4}")

    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER BEI DER DNA-ANALYSE: {fehler}")

print("\n⚙️ Diagnose-Modul abgeschlossen: Tabellen-DNA erfolgreich verifiziert.")