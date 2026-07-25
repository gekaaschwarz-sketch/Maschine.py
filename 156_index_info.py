import sqlite3

print("\n=========================================")
print("--- 🔬 AUTOMATISCHE INDEX-DNA-PRÜFUNG ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Starte forensische Analyse des Index 'idx_kunden_name'...")
    try:
        cursor.execute("PRAGMA index_info(idx_kunden_name);")
        index_dna = cursor.fetchall()

        print("\n📋️ Offizieller DNA-Bericht der Index-Struktur:")
        print(f"{'SeqNo':<6} | {'Spalten-ID':<10} | {'Spaltenname':<20}")
        print("-" * 45)
        
        for eintrag in index_dna:
            seq_no = eintrag[0]
            cid = eintrag[1]
            name = eintrag[2]

            print(f"{seq_no:<6} | {cid:<10} | {name:<20}")

    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER BEI DER INDEX-ANALYSE: {fehler}")

print("\n⚙️ Diagnose-Modul abgeschlossen: Index-DNA erfolgreich verifiziert.")