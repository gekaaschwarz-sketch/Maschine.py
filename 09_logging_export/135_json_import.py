import sqlite3
import json

print("\n=========================================")
print("--- 📥️ SQL TRESOR-IMPORT AUS JSON ---")
print("=========================================")

try:
    with open("kunden_bereitstellung.json", mode="r", encoding="utf-8") as datei:
        neu_daten = json.load(datei)

    with sqlite3.connect("speditions_tresor.db") as verbindung:
        cursor = verbindung.cursor()

        print("\n📥️ Starte automatisierten JSON-Import...")
        for kunde in neu_daten:
            name_aus_json = kunde["firmenname"]
            lkw_aus_json = kunde["lkw_id"]

            cursor.execute("INSERT OR IGNORE INTO kunden (name, zugeordneter_lkw) VALUES (?, ?)", (name_aus_json, lkw_aus_json))

            if cursor.rowcount > 0:
                print(f"✔️ NEU: {name_aus_json} erfolgreich aus JSON importiert!")
            else:
                print(f"⚠️ IGNORE: {name_aus_json} existiert bereits in Tresor.")

        verbindung.commit()

except Exception as fehler:
    print(f"🚨 SYSTEM-FEHLER BEIM IMPORT: {fehler}")

print("\n⚙️ JSON-Pipeline abgeschlossen: Datensynchronisation beendet.")