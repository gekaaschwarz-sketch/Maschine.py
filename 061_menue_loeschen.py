import json

def zeige_flotte():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
        print("\n--- 🚛️ AKTUELLE FLOTTE ---")
        for lkw in flotte:
            print(f"ID: {lkw ['ID']} | Fahrer*in: {lkw['Fahrer_in']} | Last: {lkw['Last']} kg")
    except FileNotFoundError:
        print("❌️ Keine Datenbank gefunden.")

def lkw_loeschen(ziel_id):
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)

        gefunden = False
        for lkw in flotte:
            if lkw["ID"] == ziel_id:
                flotte.remove(lkw)
                gefunden = True
                break

        if  gefunden:
            with open("flotten_datenbank.json", "w") as f:
                json.dump(flotte, f, indent=4)
            print(f"✅️ Erfolg: LKW {ziel_id} wurde gelöscht.")
        else:
            print(f"⚠️ ID {ziel_id} nicht gefunden.")
    except FileNotFoundError:
        print("❌️ Keine Datenbank gefunden.")

# --- HAUPTSCHLEIFE ---

while True:
    print("\n--- SPEDITION HAMBURG TERM V3 ---")
    print("1: Flotte anzeigen")
    print("2: LKW ausmustern (Löschen)")
    print("4: Beenden")

    auswahl = input("\nAuswahl: ")

    if auswahl == "1":
        zeige_flotte()
    elif auswahl == "2":
        l_id = input("Welche LKW-ID löschen? ")
        lkw_loeschen(l_id)
    elif auswahl == "4":
        print("Tschüss, Valentin!")
        break
    else:
        print("❌️ Ungültige Auswahl!")
