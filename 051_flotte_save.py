import json

flotte = [
    {"ID": "HH-01", "Fahrer_in": "Valentin", "Last": 2500},
    {"ID": "HH-02", "Fahrer_in": "Yvonne", "Last": 1200},
    {"ID": "HH-03", "Fahrer_in": "Stefan", "Last": 3800}
]

def flotte_speichern(daten):
    with open("flotten_datenbank.json", "w") as f:
        json.dump(daten, f, indent=4)
    print("✅️ Erfolg: Alle LKW-Daten wurden in der Datenbank gesichert!")

# Start
flotte_speichern(flotte)
