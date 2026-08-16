import sqlite3
import os

print("\n=========================================")
print("--- 🧹 SQL-DATENBANK-VAKUUMIERUNG ---")
print("=========================================")

datenbank_datei = "speditions_tresor.db"

try:
    groesse_vorher = os.path.getsize(datenbank_datei)
    print(f"📊 Dateigröße vor dem Staubsaugen: {groesse_vorher} Bytes")

    with sqlite3.connect(datenbank_datei) as verbindung:
        verbindung.isolation_level = None
        cursor = verbindung.cursor()

        print("\n⚡️ Zünde Hochleistungs-Staubsauger (VACUUM)...")
        cursor.execute("VACUUM;")
        print("🧹 SUCCESS: Totraum-Speicher erfolgreich eliminiert!")

    groesse_nachher = os.path.getsize(datenbank_datei)
    print(f"📊 Dateigröße nach dem Staubsauger: {groesse_nachher} Bytes")

except Exception as fehler:
    print(f"🚨 SYSTEM-FEHLER BEIM VAKUUMIEREN: {fehler}")

print("\n⚙️ Vakuum-Modul abgeschlossen: Stahlschrank optimal komprimiert.")