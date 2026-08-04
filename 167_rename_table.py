import sqlite3

print("\n==========================================")
print("--- ⚙️ AUTOMATISCHE TABELLEN-UMBENENNUNG ---")
print("==========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()
    
    print("\n⚡️ Starte globales Rebranding der Tabellen-Infrastruktur...")
    try:
        # Das mächtige Zahnrad benennt die gesamte Tabelle auf Englisch um:
        cursor.execute("ALTER TABLE lkw_flotte RENAME TO fleet_trucks;")
        verbindung.commit()
        print("💎 SUCCESS: Tabelle erfolgreich in 'fleet_trucks' umbenannt!")
        
        # Zur absoluten Kontrolle nutzen wir dein System-Scan-Werkzeug aus Lektion 157!
        print("\n📋️ Überprüfe aktuelle Tabellen-Auflistung im System-Master:")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tabellen = cursor.fetchall()
        
        for index, name in enumerate(tabellen, start=1):
            print(f"📦️ Tabelle {index}: {name[0]}")
            
    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER BEIM TABELLEN-RENAME: {fehler}")

print("\n⚙️ Rebranding-Modul abgeschlossen: Tabellen-Struktur erfolgreich internationalisiert.")