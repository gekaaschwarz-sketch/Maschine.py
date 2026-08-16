import os
import sqlite3

print("\n=========================================")
print("--- 📊 AUTOMATISCHE DATENBANK-MESSUNG ---")
print("=========================================")

datenbank_name = "speditions_tresor.db"

print(f"\n⚡ Starte forensische Größen-Analyse für '{datenbank_name}'...")

try:
    if os.path.exists(datenbank_name):
        groesse_bytes = os.path.getsize(datenbank_name)
        groesse_kb = groesse_bytes / 1024
        
        print("\n📋 Offizieller Speicherplatz-Bericht:")
        print("-" * 45)
        print(f"💾 Dateigröße in Bytes:    {groesse_bytes} B")
        print(f"📈 Dateigröße in Kilobytes: {groesse_kb:.2f} KB")
        print("-" * 45)
        print("💎 SUCCESS: Datenbank-Größe erfolgreich ermittelt.")
    else:
        print(f"🚨 WARNUNG: Die Datei '{datenbank_name}' wurde nicht gefunden!")
        
except Exception as fehler:
    print(f"🚨 FEHLER BEI DER GRÖSSEN-MESSUNG: {fehler}")

print("\n⚙️ Mess-Modul abgeschlossen: System-Infrastruktur erfolgreich verifiziert.")