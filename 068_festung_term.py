import json

# Wächter 1: Namens-Schutz
def hole_sauberen_namen():
    while True:
        name = input("Name der Fahrer*in: ")
        if name.isalpha():
            return name
        else:
            print("❌️ Fehler: Nur Buchstaben erlaubt!")

# Wächter 2: Gewichts-Schutz (NEU IN MENÜ!)
def hole_validierte_last():
    while True:
        try:
            last = int(input("Ladung in kg (0-40000): "))
            if 0 <= last <= 40000:
                return last
            else:
                print("❌️ Fehler: Gewicht unlogisch (0 bis 40.000 kg)!")
        except ValueError:
            print("❌️ Fehler: Bitte nur ganze Zahlen eingeben!")

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

# Option 2: LKW hinzufügen (JETZT VOLLSTÄNDIG GESICHERT!)
def lkw_hinzufuegen():
    with open("flotten_datenbank.json", "r") as f:
        flotte = json.load(f)
    print("\n--- NEUEN LKW REGISTRIEREN ---")
    while True:
        neue_id = input("Neue LKW-ID (z.B. HH-05): ")
        if neue_id in [lkw["ID"] for lkw in flotte]:
            print(f"❌️ Fehler: Die ID {neue_id} ist bereits vergeben!")
        else:
            break
    neue_person = hole_sauberen_namen()

    # HIER WIRKT JETZT DER NEUE WÄCHTER:
    neue_last = hole_validierte_last()

    flotte.append({"ID": neue_id, "Fahrer_in": neue_person, "Last": neue_last})
    with open("flotten_datenbank.json", "w") as f:
        json.dump(flotte, f, indent=4)
    print(f"✅️ {neue_person} wurde erfolgreich registriert!")

# --- HAUPTSCHLEIFE ---
while True:
    print("\n==============================")
    print("--- SPEDITION HAMBURG V8 ---")
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
        print("❌️ Ungültige Auswahl!")
