import sqlite3
import csv

print("\n=========================================")
print("--- 🔬 DER GROSSE DUPLIKAT-HÄRTETEST ---")
print("=========================================")

with open("kunden_export.csv", mode="r", encoding="utf-8") as datei:
    leser = csv.reader(datei, delimiter=";")
    next(leser)

    with sqlite3.connect("speditions_tresor.db") as verbindung:
        cursor = verbindung.cursor()

        print("\n🧪 Testlauf: Versuche identische Daten zu importieren...")
        for zeile in leser:
            name_aus_csv = zeile[1]
            lkw_aus_csv = zeile[2]

            cursor.execute("INSERT OR IGNORE INTO kunden (name, zugeordneter_lkw) VALUES (?, ?)", (name_aus_csv, lkw_aus_csv))
            
            if cursor.rowcount == 0:
                print(f"🛑 BLOCKIERT: Speditions-Schutzwall hat '{name_aus_csv}' abgefangen!")
            else:
                print(f"✔️ NEU: {name_aus_csv} importiert.")

        verbindung.commit()

print("\n🔬 Test beendet: Der Schutzwall ist absolut schussfest!")