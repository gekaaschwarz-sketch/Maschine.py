import sqlite3
import csv

print("\n=========================================")
print("--- 📥️ SQL TRESOR-EXPORT NACH EXCEL ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()
    cursor.execute("SELECT * FROM kunden")
    kunden_daten = cursor.fetchall()

with open("kunden_export.csv", mode="w", newline="", encoding="utf-8") as datei:
    schreiber = csv.writer(datei, delimiter=";")

    schreiber.writerow(["Kunden_ID", "Firmenname", "Zugeordneter_LKW"])

    schreiber.writerows(kunden_daten)

print("\n✔️ Export erfolgreich! Die Daten 'kunden_export.csv' wurde für Excel geschmidet.")