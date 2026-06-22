import json

def lkw_komplett_loeschen(ziel_id):
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)

        ursprung_laenge = len(flotte)
        # Eine neue Liste bauen, die nur die LKWs enthält, die NICHT gelöscht werden sollen
        bereinigte_flotte = [lkw for lkw in flotte if lkw["ID"] != ziel_id]

        if len(bereinigte_flotte) < ursprung_laenge:
            with open("flotten_datenbank.json", "w") as f:
                json.dump(bereinigte_flotte, f, indent=4)
            print(f"✅️ Erfolg: Alle LKW-Einträge mit der ID {ziel_id} wurden restlos entfernt.")
        else:
            print(f"⚠️ ID {ziel_id} nicht in der Datenbank gefunden.")

    except FileNotFoundError:
        print("❌️ Keine Datenbank-Datei gefunden.")

# Testlauf
print("--- COCKPIT: RADIKAL-LÖSCHUNG ---")
zeige_id = input("Welche ID komplett entfernen?: ")
lkw_komplett_loeschen(zeige_id)
