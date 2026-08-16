import shutil
import os

print("\n=========================================")
print("--- 💾 AUTOMATISCHES DATEN-BACKUP ---")
print("=========================================")

quell_datei = "speditions_tresor.db"
ziel_datei = "speditions_tresor_BACKUP.db"

try:
    if os.path.exists(quell_datei):
        print(f"🔍️ Stamm-Tresor '{quell_datei}' gefunden.")

        shutil.copy2(quell_datei, ziel_datei)

        print("\n💾 SUCCESS: Vollautomatisches Backup erfolgreich geschmiedet")
        print(f"📁 Sicherungskopie liegt bereit als: '{ziel_datei}'")
    else:
        print(f"⚠️ FEHLER: Die Datei '{quell_datei}' wurde nicht gefunden! Kein Backup möglich.")

except Exception as fehler:
    print(f"🚨 KRITISCHER DATEI-FEHLER: {fehler}")

print("\n⚙️ Backup-Modul abgeschlossen: Daten für den Ernstfall gesichert.")