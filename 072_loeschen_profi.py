import json

# Option 1: Flotte anzeigen
def zeige_flotte():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
        print("\n--- 🚛️ AKTUELLE FLOTTE ---")
        for lkw in flotte:
            print(f"ID: {lkw['ID']} | Fahrer*in: {lkw['Fahrer_in']} | Last: {lkw['Last']} kg")
    except FileNotFoundError:
        print("❌️ Keine Datenbank gefunden.")

# Option 3: LKW KOMPLETT LÖSCHEN (NEU!)
def lkw_loeschen():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
    except FileNotFoundError:
        print("❌️ Keine Datenbank vorhanden. Löschen nicht möglich.")
        return

    print("\n--- 🗑️ LKW AUS SYSTEM LÖSCHEN ---")
    loesch_id = input("Welche LKW-ID soll gelöscht werden? (oder 'zurück'): ")

    if loesch_id.lower() == "zurueck":
        return

    # Wir suchen, ob die ID überchaupt in der Liste existiert
    lkw_gefunden = None
    for lkw in flotte:
        if lkw["ID"] == loesch_id:
            lkw_gefunden = lkw
            break

    if lkw_gefunden:
        # Der Sichercheits-Wächter fragt nach!
        bestaetigung = input(f"⚠️ Sicher? LKW {loesch_id} von {lkw_gefunden['Fahrer_in']} wirklich löschen? (ja/nein): ")

        if bestaetigung.lower() == "ja":
            flotte.remove(lkw_gefunden) # Radikale Löschung aus der Liste!
            with open("flotten_datenbank.json", "w") as f:
                json.dump(flotte, f, indent=4)
            print(f"🗑️ LKW {loesch_id} wurde erfolgreich aus dem System gelöscht!")
        else:
            print("❌️ Löschvorgang abgebrochen.")
    else:
        print(f"❌️ Fehler: Die ID {loesch_id} existiert nicht in der Flotte!")

# --- HAUPTSCHLEIFE ---
while True:
    print("\n==============================")
    print("--- SPEDITION HAMBURG V12 ---")
    print("==============================")
    print("1: Flotte anzeigen")
    print("3: LKW löschen")
    print("4: Beenden")

    auswahl = input("\nDeine Auswahl: ")
    if auswahl == "1":
        zeige_flotte()
    elif auswahl == "3":
        lkw_loeschen()
    elif auswahl == "4":
        print("Tschüss, Valentin!")
        break
