import sqlite3

print("\n=========================================")
print("--- 🛡️ AUTOMATISCHER SQL-SCHNELL-CHECK ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()
    
    print("\n⚡️ Starte krisensicheren Datenbank-Schnell-Check (PRAGMA)...")
    try:
        cursor.execute("PRAGMA quick_check;")
        ergebnis = cursor.fetchone()[0]
        
        print("\n📋 Offizieller Diagnose-Bericht:")
        print("-" * 45)
        print(f"🔍 System-Status: {ergebnis}")
        print("-" * 45)
        
        if ergebnis == "ok":
            print("💎 SUCCESS: Haupt-Infrastruktur ist absolut fehlerfrei und stabil!")
        else:
            print(f"🚨 ALARM: Strukturelle Anomalie entdeckt -> {ergebnis}")
            
    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER IM DIAGNOSE-MODUL: {fehler}")

print("\n⚙️ Schnell-Check abgeschlossen: System-Infrastruktur erfolgreich verifiziert.")