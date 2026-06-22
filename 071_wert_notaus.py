import json

# Wächter 1: Namens-Schuts MIT NOTAUS-SYSTEM!
def hole_sauberen_namen():
    while True:
        name = input("Name der Fahrer*in (oder 'zurueck' zum Abbrechen): ")
        if name.lower() == "zurueck":
            return "ABBRUCH"
        if name.isalpha():
            return name
        else:
            print("❌️ Fehler: Nur Buchstaben erlaubt! Tippe 'zuruek' zum Hauptmenü.")

# Wächter 2: Gewicht-Schutz MIT TRY-EXCEPT UND NOTAUS! (NEU!)
def hole_validierte_last():
    while True:
        eingabe = input("Ladung in kg (0-40000 oder 'zurueck'): ")
        if eingabe.lower() == "zurueck":
            return "ABBRUCH"
        try:
            last = int(eingabe)
            if 0 <= last <= 40000:
                return last
            else:
                print("❌️ Fehler: Gewicht unlogisch (0 bis 40.000 kg)!")
        except ValueError:
            print("❌️ Fehler: Bitte nur ganze Zahlen oder 'zurueck' eingeben!")

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

# Optionen 2: LKW hinzufuegen mit DREIFACH-CHEF-SCHUTZ!
def lkw_hinzufuegen():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
    except FileNotFoundError:
            flotte = []

    print("\n--- NEUEN LKW REGISTRIEREN ---")

    # 1. NOTAUS BEI DER ID
    neue_id = input("Neue LKW-ID (oder 'zurueck' zum Abbrechen): ")
    if neue_id.lower() == "zurueck":
        print("⚠️ Registrierung bei ID-Eingaben abgebrochen!")
        return

    # 2. NOTAUS BEIM NAMEN
    neue_person = hole_sauberen_namen()
    if neue_person == "ABBRUCH":
        print("⚠️ Registrierung bei Namens-Eingabe abgebrochen!")
        return

    # 3. NOTAUS & INPUT-SCHUTZ BEIM GEWICHT (Hier greift der neue Wächter!)
    neue_last = hole_validierte_last()
    if neue_last == "ABBRUCH":
        print("⚠️ Registrierung bei Gewichts-Eingabe abgebrochen!")
        return

    flotte.append({"ID": neue_id, "Fahrer_in": neue_person, "Last": neue_last})
    with open("flotten_datenbank.json", "w") as f:
        json.dump(flotte, f, indent=4)
    print(f"✅️ {neue_person} wurde erfolgreich mit {neue_last} kg registriert!")

# --- HAUPTSCHLEIFE ---
while True:
    print("\n==============================")
    print("--- SPEDITION HAMBURG V11 ---")
    print("==============================")
    print("1: Flotte anzeigen")
    print("2: Neuen LKW registrieren")
    print("4: Beenden")

    auswahl = input("\nDeine Auswahl: ")
    if auswahl == "1":
        zeige_flotte()
    elif auswahl == "2":
        lkw_hinzufuegen()
    elif auswahl == "4":
        print("System wird sicher heruntergefahren. Tschüss, Valentin!")
        break
    else:
        print("❌️ Ungültige Auswahl")
