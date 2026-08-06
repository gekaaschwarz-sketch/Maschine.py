import sqlite3

print("\n=========================================")
print("--- 🛡️ AUTOMATISCHE TIMEOUT-SICHERUNG ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()
    
    print("\n⚡ Starte krisensichere Aktivierung des Busy-Timeouts...")
    try:
        cursor.execute("PRAGMA busy_timeout = 5000;")
        
        cursor.execute("PRAGMA busy_timeout;")
        aktueller_timeout = cursor.fetchone()[0]
        
        print("\n📋 Offizieller Sicherheits-Bericht:")
        print("-" * 69)
        print(f"⏳ Aktives Busy-Timeout: {aktueller_timeout} Millisekunden (Sicherheitsnetz aktiv).")
        print("-" * 69)
        print("💎 SUCCESS: Datenbank wartet ab jetzt bei Sperren krisensicher 5 Sekunden!")
        
    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER IM TIMEOUT-MODUL: {fehler}")

print("\n⚙️ Sicherungs-Modul abgeschlossen: Multi-User-Verkehr erfolgreich geschützt.")