import json 

#Wächter 1: Namens-Schuty MIT NOTAUS-SYSTEM
def hole_sauberen_namen():
    while True:
        name = input("Name der Fahrer*in (oder 'zurueck' zum Abbrechen): ")
        if name.lower() == "zurueck":
            return "ABBRUCH"
        if name.isalpha():
            return name
        else:
            print("❌️ Fehler: Nur Buchstaben erlaubt! Tippe 'zurueck' zum Hauptmenü.")

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

# Option 2: LKW hinzufügen mit DOPPEL-NOTAUS!
def lkw_hinzufuegen():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
    except FileNotFoundError:
        flotte = []

    print("\n--- NEUEN LKW REGISTRIEREN ---")

    # 1. NOTAUS DIREKT BEI DER ID:
    neue_id = input("Neue LKW-ID (oder 'zurueck' zum Abbrechen): ")
    if neue_id.lower() == "zurueck":
        print("⚠️ Registrierung bei ID-Eingabe abgebrochen! Zurück zum Hauptmenü.")
        return # Abbruch 1!

    # 2. NOTAUS BEIM NAMEN:
    neue_person = hole_sauberen_namen()
    if neue_person == "ABBRUCH":
        print("⚠️ Registrierung bei Namens-Eingabe abgebrochen! Zurück zum Hauptmenü.")
        return # Abbbruch 2!

    last = int(input("Ladung in kg: "))
    flotte.append({"ID": neue_id, "Fahrer_in": neue_person, "Last": last})
    with open("flotten_datenbank.json", "w") as f:
        json.dump(flotte, f, indent=4)
    print(f"✅️ {neue_person} wurde erfolgreich registriert!")

# --- HAUPTSCHLEIFE ---
while True:
    print("\n==============================")
    print("--- SPEDITION HAMBURG V10 ---")
    print("==============================")
    print("1: Flottte anzeigen")
    print("2: Neue LKW registrieren")
    print("4: Beenden")

    auswahl = input("\nDeine Selection: ")
    if auswahl == "1":
        zeige_flotte()
    elif auswahl == "2":
        lkw_hinzufuegen()
    elif auswahl == "4":
        print("System wird sicher heruntergefahren. Tschüss, Valentin!")
        break
    else:
        print("❌️ Ungültige Auswahl")
