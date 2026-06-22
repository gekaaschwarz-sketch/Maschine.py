import json # Das neue Werkzeug laden

# Unsere Frachtdaten als Dictionary
fracht_daten = {
    "LKW_ID": "HH-VK-2026",
    "Fahrer_in": "Valentin",
    "Ladung": "Stahlrollen",
    "Gewicht": 2500
}

#Speichern als JSON-Datei
def daten_export(daten):
    with open("frachtbrief.json", "w") as f:
        json.dump(daten, f, indent=4) # indent=4 macht es schön lesbar
    print("✅️ Frachtbrief wurde als JSON gespeichert!")

# Start
daten_export(fracht_daten)
