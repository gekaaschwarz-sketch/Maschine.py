import sqlite3
import json

print("\n=========================================")
print("--- SQL-TRESOR-EXPORT NACH JSON ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    verbindung.row_factory = sqlite3.Row
    cursor = verbindung.cursor()

    cursor.execute("SELECT name, zugeordneter_lkw FROM kunden")
    kunden_zeilen = cursor.fetchall()

    export_liste = []
    for zeile in kunden_zeilen:
        export_liste.append({
            "firmenname": zeile["name"],
            "lkw_id": zeile["zugeordneter_lkw"]
        })

with open("kunden_bereitstellung.json", mode="w", encoding="utf-8") as datei:
    json.dump(export_liste, datei, indent=4, ensure_ascii=False)

print("\n🌐 SUCCESS: JSON-Schnittstelle erfolgreich geschmiedet!")
print("📱 Die Datei 'kunden_bereitstellung.json' steht für die Fahrer-App bereit.")