import json

def lade_flotte():
    try:
        with open("flotten_datenbank.json", "r") as f:
            daten = json.load(f)

        print("--- 🚛️ FLOTTEN-STATUS AKTUEL ---")
        for lkw in daten:
            print("ID: " + lkw["ID"] + "| Fahrer*in: " + lkw["Fahrer_in"] + " | Last: " + str(lkw["Last"]) + " kg")

    except FileNotFoundError:
        print("❌️ Fehler: Keine Datenbank gefunden! Bitte erst 051 starten.")

# Programm-Starten
lade_flotte()
