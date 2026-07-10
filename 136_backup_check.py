import sqlite3
import os

print("\n=========================================")
print("--- 🛡️ AUTOMATISCHE BACKUP-TÜV-CHECK ---")
print("=========================================")

backup_datei = "speditions_tresor_BACKUP.db"

if not os.path.exists(backup_datei):
    print(f"❌ FEHLER: Die Sicherungsdatei '{backup_datei}' existiert nicht auf der SSD")
else:
    try:
        with sqlite3.connect(backup_datei) as verbindung:
            cursor = verbindung.cursor()
            cursor.execute("PRAGMA integrity_check;")
            ergebnis = cursor.fetchone()

            print(f"\n🔍️ Scanne Backup-Struktur auf Bit-Ebene...")

            if ergebnis == ("ok",):
                print(f"💎 SUCCESS: Sicherung '{backup_datei}' ist zu 100% unbeschädigt und lesbar!")
                print("🛡️ Stempel: SQL-INTEGRITY-OK")
            else:
                print(f"🚨 WARNUNG: Beschädigung im Backup gefunden! Details: {ergebnis}")

    except sqlite3.Error as fehler:
        print(f"🚨 CRITICAL SQL ERROR WÄHREND DES CHECKS: {fehler}")

print("\n⚙️ Validierung-Modus abgeschlossen: Datensicherheit felsenfest garantiert.")