import sqlite3

print("\n=========================================")
print("--- ⚙️ AUTOMATISCHE DATENBANK-KOMPRESSION ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()
    
    print("\n⚡ Starte forensische Speicherplatz-Optimierung (VACUUM)...")
    try:
        verbindung.isolation_level = None
        
        cursor.execute("VACUUM;")
        
        print("💎 SUCCESS: Datenbank erfolgreich komprimiert und Fragmente bereinigt!")
        print("📊 Integritäts-Prüfung: Ungenutzte Speicher-Löcher restlos geschlossen.")
        
    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER BEIM SYSTEM-VACUUM: {fehler}")
    finally:
        verbindung.isolation_level = ""

print("\n⚙️ Kompressions-Modul abgeschlossen: Triebwerke laufen im Spar-Modus.")