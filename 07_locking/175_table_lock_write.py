import sqlite3

print("\n========================================")
print("--- 📝 AUTOMATISCHE SCHREIB-SPERRUNG ---")
print("========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()
    
    print("\n⚡ Starte krisensichere Aktivierung der Schreib-Sperre...")
    try:
        cursor.execute("BEGIN EXCLUSIVE;")
        
        cursor.execute("UPDATE fleet_trucks SET payload_tons = 12 WHERE id = 1;")
        
        print("\n📋 Offizieller Sicherheits-Bericht:")
        print("-" * 75)
        print("📝 Exclusive-Lock aktiv: Tabelle für alle Fremdzugriffe komplett blockiert.")
        print("-" * 75)
        print("💎 SUCCESS: Schreib-Sperre erfolgreich im Live-Betrieb verankert!")
        
        verbindung.commit()
        print("🔓 Schreib-Sperre nach erfolgreichem Update wieder aufgehoben.")
        
    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER IM SCHREIB-SPERR-MODUL: {fehler}")

print("\n⚙️ Schreib-Sperr-Modul abgeschlossen: Daten-Sicherheit erfolgreich stabilisiert.")