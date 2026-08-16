import sqlite3
import os
import shutil

print("\n=========================================")
print("--- 🚒 AUTOMATISCHES SQL-RESTORE-MODUL ---")
print("=========================================")

live_datei = "speditions_tresor.db"
backup_datei = "speditions_tresor_BACKUP.db"

try:
    print("\n🔍️ Prüfe Verfügbarkeit der Sicherungskopie...")
    if not os.path.exists(backup_datei):
        raise FileNotFoundError(f"Die Backup-Datei '{backup_datei}' fehlt auf SSD!")

    print("🚨 SIMULATION: Der Live-Tresor ist beschädigt! Starte Notfall-Restore...")

    if os.path.exists(live_datei):
        os.remove(live_datei)
        print("🧼 Korrupte Live-Datenbank erfolgreich von der SSD gefegt.")

    shutil.copy(backup_datei, live_datei)

    print("\n🚒 SUCCESS: Der Stahlschrank wurde erfolgreich wiederhergestellt!")
    print("🚛 Das System der Hamburger Spedition ist voll einsatzbereit!")

except Exception as fehler:
    print(f"🚨 KRITISCHER RESTORE-FEHLER: {fehler}")

print("\n⚙️ Notfall-Restore-Modul abgeschlossen: Katastrophenschutz beendet.")