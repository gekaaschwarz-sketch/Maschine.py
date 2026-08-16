import sqlite3
import csv

print("\n" + "=" * 45)
print("--- 📊 AUTOMATISIERTER CO2-CSV-EXPORT ---")
print("=" * 45)

datenbank = "speditions_tresor.db"
export_datei = "flotten_export.csv"

print(f"\n⚡ Starte Daten-Extraktion aus '{datenbank}'...")

try:
    with sqlite3.connect(datenbank) as verbindung:
        cursor = verbindung.cursor()
        
        cursor.execute("PRAGMA table_info(fleet_trucks);")
        spalten = cursor.fetchall()
        header = [spalte[1] for spalte in spalten]
        
        cursor.execute("SELECT * FROM fleet_trucks;")
        alle_daten = cursor.fetchall()
        
        with open(export_datei, "w", newline="", encoding="utf-8") as f:
            schreiber = csv.writer(f, delimiter=";")
            
            schreiber.writerow(header)
            schreiber.writerows(alle_daten)
            
        print(f"💎 SUCCESS: {len(alle_daten)} Datensätze erfolgreich nach '{export_datei}' exportiert!")
        
except sqlite3.Error as fehler:
    print(f"🚨 FEHLER BEIM EXPORT-PROZESS: {fehler}")

print("\n" + "=" * 53)
print("⚙️ Export-Modul abgeschlossen: Infrastruktur bereit.")
print("=" * 53)