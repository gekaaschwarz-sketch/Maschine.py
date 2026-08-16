import json

def lkw_hinzufuegen():
    # 1. Bestehende Datenbank laden
    with open("flotten_datenbank.json", "r") as f:
        flotte = json.load(f)

    # 2. Daten für den neuen LKW abfragen
    neue_id = input("Neue LKW-ID (z.B. HH-04): ")
    neue_person = input("Name der Fahrer*in: ")
    neue_last = int(input("Ladung in kg: "))

    # 3. Den neuen LKW in die Liste packen (Deine neuer Qualitäts-Key!)
    neuer_eintrag = {"ID": neue_id, "Fahrer_in": neue_person, "Last": neue_last}
    flotte.append(neuer_eintrag)

    # 4. Die aktualisierte Liste zurück in die Datei speichern
    with open("flotten_datenbank.json", "w") as f:
        json.dump(flotte, f, indent=4)
    print(f"✅️ Erfolg: {neue_person} wurde zur Flotte hinzugefügt!")

# Start
lkw_hinzufuegen()
