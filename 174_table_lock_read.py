import sqlite3

print("\n=====================================")
print("--- 📖 AUTOMATISCHE LESE-SPERRUNG ---")
print("=====================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()
    
    print("\n⚡ Starte krisensichere Aktivierung der Lese-Sperre...")
    try:
        cursor.execute("BEGIN;")
        
        cursor.execute("SELECT * FROM fleet_trucks;")
        daten = cursor.fetchall()
        
        print("\n📋 Offizieller Sicherheits-Bericht:")
        print("-" * 45)
        print(f"📖 Shared-Lock aktiv: Daten-Zustand für Bericht eingefroren.")
        print("-" * 45)
        print("💎 SUCCESS: Lese-Sperre erfolgreich im laufenden Betrieb verankert!")
        
        verbindung.commit()
        print("🔓 Lese-Sperre nach erfolgreichem Bericht wieder aufgehoben.")
        
    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER IM LESE-SPERR-MODUL: {fehler}")

print("\n⚙️ Lese-Sperr-Modul abgeschlossen: Bericht-Konsistenz erfolgreich gesichert.")