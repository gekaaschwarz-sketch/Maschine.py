import sqlite3
import csv

print("\n=========================================")
print("--- 🛡️ SQL-DUPLIKAT-SCHUTZWALL v1.0 ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_kunden_name ON kunden(name)")
    verbindung.commit()
with open("kunden_export.csv", mode="r", encoding="utf-8") as datei:
    leser = csv.reader(datei, delimiter=";")
    next(leser)

    with sqlite3.connect("speditions_tresor.db") as verbindung:
        cursor = verbindung.cursor()

        print("\n📥️ Starte duplikat-sicheren Daten-Import...")
        for zeile in leser:
            name_aus_csv = zeile[1]
            lkw_aus_csv = zeile[2]

            cursor.execute("INSERT OR IGNORE INTO kunden (name, zugeordneter_lkw) VALUES (?, ?)", (name_aus_csv, lkw_aus_csv))

            if cursor.rowcount > 0:
                print(f"✔️ NEU: {name_aus_csv} erfolgreich importiert!")
            else:
                print(f"⚠️ BLOCKIERT: {name_aus_csv} existiert bereits! Duplikat verhindert.")

        verbindung.commit()

print("\n⚙️ Pipeline-Schutzwall aktiv: Keine doppelten Datensätze zugelassen.")