import shutil
import os
from datetime import datetime

LINIE = "=" * 45

DB_DATEI = "speditions_tresor.db"
BACKUP_ORDNER = "backups"
MAX_BACKUPS = 3

print("\n" + LINIE)
print("--- 🔄 AUTOMATISIERTE BACKUP-ROTATION ---")
print(LINIE)

try:
    os.makedirs(BACKUP_ORDNER, exist_ok=True)

    zeitstempel = datetime.now().strftime("%Y%m%d_%H%M%S")
    neuer_name = f"{BACKUP_ORDNER}/tresor_backup_{zeitstempel}.db"

    shutil.copy2(DB_DATEI, neuer_name)
    print(f"💾 Neues Backup erstellt: {neuer_name}")

    vorhandene_backups = sorted(
        f for f in os.listdir(BACKUP_ORDNER) if f.startswith("tresor_backup_")
    )

    print(f"📋 Aktuell vorhandene Backups: {len(vorhandene_backups)}")

    while len(vorhandene_backups) > MAX_BACKUPS:
        aeltestes = vorhandene_backups.pop(0)
        pfad = os.path.join(BACKUP_ORDNER, aeltestes)
        os.remove(pfad)
        print(f"🗑️ Ältestes Backup gelöscht: {aeltestes}")

    print(f"✅ Rotation abgeschlossen: {len(vorhandene_backups)} Backups vorhanden.")

except Exception as fehler:
    print(f"🚨 FEHLER BEI DER BACKUP-ROTATION: {fehler}")

print("\n" + LINIE)
print("⚙️ Backup-Modul abgeschlossen.")
print(LINIE)