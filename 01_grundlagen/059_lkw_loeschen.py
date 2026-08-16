import json

def lkw_loeschen(ziel_id):
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)

        # Wir suchen den LKW mit der passenden ID
        gefunden = False
        for lkw in flotte:
            if lkw["ID"] == ziel_id:
                flotte.remove(lkw)
                gefunden = True
                break # Schleife abbrechen, wenn gelöscht

        if gefunden:
            # Die neue Liste ohne den gelöschten LKW speichern
            with open("flotten_datenbank.json", "w") as f:
                json.dump(flotte, f, indent=4)
            print(f"✅️ Erfolg: LKW mit der ID {ziel_id} wurde aus der Datenbank gelöscht.")
        else:
            print(f"⚠️ LKW mit ID {ziel_id} wurde in der Datenbank nicht gefunden.")

    except FileNotFoundError:
        print("❌️ Fehler: Keine Datenbank-Datei gefunden.")

# Testlauf
print("--- SYSTEM-OPERATION: FAHRZEUG LÖSCHEN ---")
loesch_id = input("Welche LKW-ID soll gelöscht werden? (z.B. HH-04): ")
lkw_loeschen(loesch_id)
