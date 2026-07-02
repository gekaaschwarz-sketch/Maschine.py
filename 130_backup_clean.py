import os

print('\n=========================================')
print("--- 🧹 BACKUP-SPEICHER-BEREINIGUNG ---")
print("=========================================")

backup_datei = "speditions_tresor_BACKUP.db"

try:
    if os.path.exists(backup_datei):
        print(f"🔍️ Alte Sicherungsdatei '{backup_datei}' gefunden.")

        os.remove(backup_datei)

        print(f"\n🧹 SUCCESS: '{backup_datei}'")
        print("💾 Der Speicherplatz wurde für das nächste Backup freigegeben.")
    else:
        print(f"ℹ️ INFO: Keine alte Sicherungskopie vorhanden. Der Tisch ist sauber.")

except Exception as fehler:
    print(f"🚨 KRITISCHER DATEI-FEHLER: {fehler}")

print("\n⚙️ Bereinigungs-Modul abgeschlossen: Festplatte optimierer.")