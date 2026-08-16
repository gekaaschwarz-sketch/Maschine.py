import sqlite3

print("\n==========================================")
print("--- 🗑️ AUTOMATISCHE TABELLEN-VERNICHTUNG ---")
print("==========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()
    
    print("\n⚡ Starte Bereinigung veralteter Datenbank-Fragmente...")
    try:
        cursor.execute("DROP TABLE IF EXISTS lkw_flotte_backup_snapshot;")
        verbindung.commit()
        print("💎 SUCCESS: Altar Backup-Snapshot restlos von der SSD gefegt!")
        
        print("\n📋 Überprüfe verbleibende Tabellen-Infrastruktur:")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tabellen_liste = cursor.fetchall()
        
        for index, tabelle in enumerate(tabellen_liste, start=1):
            print(f"📦 Tabelle {index}: {tabelle[0]}")
            
    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER BEI DER DATA-BEREINIGUNG: {fehler}")

print("\n⚙️ Bereinigungs-Modul abgeschlossen: System-Infrastruktur erfolgreich entschlackt.")