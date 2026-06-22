import json

def gewicht_aktualisieren(neues_gewicht):
    # 1. Datei einlesen
    with open("frachtbrief.json", "r") as f:
        daten = json.load(f)

    # 2. Den Wert im Dictionary änder
    daten["Gewicht"] = neues_gewicht
    print("Änderung: Gewicht auf " + str(neues_gewicht) + " kg gesetzt.")

    # 3. Datei wieder speichern
    with open("fracht.json", "w") as f:
        json.dump(daten, f, indent=4)
    print("✅️ JSON-Datei wurde erfolgreich aktualisiert!")

# Test: Wir ändern das Gewicht auf 3200 kg
gewicht_aktualisieren(3200)
