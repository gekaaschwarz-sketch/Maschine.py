import sqlite3
import csv

print("\n=========================================")
print("--- 📥️ SQL TRESOR-IMPORT AUS EXCEL ---")
print("=========================================")

with open("kunden_export.csv", mode="r", encoding="utf-8") as datei:
    leser = csv.reader(datei, delimiter=";")

    next(leser)

    with sqlite3.connect("speditions_tresor.db") as verbindung:
        cursor = verbindung.cursor()

        print("\n📥️ Starte automatisierten Daten-Import...")
        for zeile in leser:
            name_aus_csv = zeile[1]
            lkw_aus_csv = zeile[2]

            cursor.execute("INSERT INTO kunden (name, zugeordneter_lkw) VALUES (?, ?)", (name_aus_csv, lkw_aus_csv))
            print(f"✔️ {name_aus_csv} erfolgreich aus Excel in den Tresor importiert!")

        verbindung.commit()

print("\n⚙️ Pipeline abgeschlossen: Alle Excel-Daten wurden krisensicher synchronisiert.")