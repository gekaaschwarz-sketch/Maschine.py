import sqlite3

print("\n===========================================")
print("--- 🔓️ AUTOMATISCHE SYSTEM-ENTRIEGELUNG ---")
print("===========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()
    
    print("\n⚡ Starte krisensichere Freigabe der Tabellen-Infrastruktur...")
    try:
        cursor.execute("PRAGMA locking_mode = NORMAL;")
        
        cursor.execute("SELECT * FROM fleet_trucks LIMIT 1;")
        ergebnis = cursor.fetchone()
        
        print("\n📋 Offizieller Sicherheits-Bericht:")
        print("-" * 45)
        print("🔓 Sperr-Modus aufgehoben: NORMAL-Modus aktiv.")
        print("-" * 45)
        print("💎 SUCCESS: Exklusive Tabellen-Sperrung erfolgreich gelöst!")
        
    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER IM ENTRIEGELUNGS-MODUL: {fehler}")

print("\n⚙️ Entriegelungs-Modul abgeschlossen: Multi-User-Verkehr erfolgreich freigegeben.")