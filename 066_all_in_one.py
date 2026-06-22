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

# Option 2: LKW hinzufügen (Mit ID-Schutz!)
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
    neue_last = int(input("Ladung in kg: "))
    flotte.append({"ID": neue_id, "Fahrer_in": neue_person, "Last": neue_last})
    with open("flotten_datenbank.json", "w") as f:
        json.dump(flotte, f, indent=4)
    print(f"✅️ {neue_person} wurde erfolgreich registriert!")

# Option 3: Radikal-Löschen (Der Schleifen-Fix integriert!)
def lkw_komplett_loeschen():
    with open("flotten_datenbank.json", "r") as f:
        flotte = json.load(f)
    print("\n--- LKW AUSMUSTERN (RADIKAL-LÖSCHUNG) ---")
    ziel_id = input("Welche ID komplett aus dem System entfernen?: ")
    ursprung_laenge = len(flotte)
    bereinigte_flotte = [lkw for lkw in flotte if lkw["ID"] != ziel_id]

    if len(bereinigte_flotte) < ursprung_laenge:
        with open("flotten_datenbank.json", "w") as f:
            json.dump(bereinigte_flotte, f, indent=4)
        print(f"✅️ Erfolg: Alle Einträge mit ID {ziel_id} wurden gelöscht.")
    else:
        print(f"⚠️ ID {ziel_id} nicht in der Datenbank gefunden.")

# --- HAUPTSCHLEIFE ---
while True:
    print("\n==============================")
    print("--- SPEDITION HAMBURG V7 ---")
    print("==============================")
    print("1: Flotte anzeigen")
    print("2: Neuen LKW registrieren")
    print("3: LKW ausmustern (Radikal-Löschen)")
    print("4: Beenden")

    auswahl = input("\nDeine Auswahl: ")
    if auswahl == "1":
        zeige_flotte()
    elif auswahl == "2":
        lkw_hinzufuegen()
    elif auswahl == "3":
        lkw_komplett_loeschen()
    elif auswahl == "4":
        print("System wird sicher herunterfahren. Tschüss, Valentin!")
        break
    else:
        print("❌️ Ungültige Auswahl!")
