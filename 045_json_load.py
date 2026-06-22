import json

def daten_import():
    try:
        with open("frachtbrief.json", "r") as f:
            geladene_daten = json.load(f)

        print("--- FRACHTBRIEF GELADEN ---")
        print("Fahrer*in: " + geladene_daten["Fahrer_in"])
        print("Ladung: " + geladene_daten["Ladung"])
        print("Gewicht: " + str(geladene_daten["Gewicht"]) + " kg")

    except FileNotFoundError:
        print("❌️ Fehler: Frachtbrief wurde nicht gefunden")

# Start
daten_import()
