import json

# Wächter 1: Namens-Schutz
def hole_sauberen_namen():
    while True:
        name = input("Name der Fahrer*in: ")
        if name.isalpha():
            return name
        else:
            print("❌️ Fehler: Nur Buchstaben erlaubt!")

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

# Option 2: LKW hinzufügen (JETZT MIT ID-SCHUTZ!)
def lkw_hinzufuegen():
    with open("flotten_datenbank.json", "r") as f:
        flotte = json.load(f)

    # Der ID-Doppelgänger-Schutz
    while True:
        neue_id = input("Neue LKW-ID (z.B. HH-04): ")
        # Prüfen, ob die ID schon existiert
        if neue_id in [lkw["ID"] for lkw in flotte]:
            print(f"❌️ Fehler: Die ID {neue_id} ist bereits vergeben!")
        else:
            break # ID ist frei, Schleife verlassen!

    neue_person = hole_sauberen_namen()
    neue_last = int(input("Ladung in kg: "))

    neuer_lkw = {"ID": neue_id, "Fahrer_in": neue_person, "Last": neue_last}
    flotte.append(neuer_lkw)

    with open("flotten_datenbank.json", "w") as f:
        json.dump(flotte, f, indent=4)
    print(f"✅️ {neue_person} wurde erfolgreich registriert!")

# --- HAUPTSCHLEIFE ---
while True:
    print("\n==============================")
    print("--- SPEDITION HAMBURG V6 ---")
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
