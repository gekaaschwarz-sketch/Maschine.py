import json

# Wächter: Namens-Schutz
def hole_sauberen_namen():
    while True:
        name = input("Name der Fahrer*in: ")
        if name.isalpha():
            return name
        else:
            print("❌️ Fehler: Nur Buchstaben erlauben!")

# Option 1: Flotte anzeigen
def zeige_flotte():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
        print("\n--- 🚛️ AKTUELLE FLOTTE")
        for lkw in flotte:
            print(f"ID: {lkw['ID']} | Fahrer*in: {lkw['Fahrer_in']} | Last: {lkw['Last']} kg")
    except FileNotFoundError:
        print("❌️ Keine Datenbank gefunden.")

# Option 2: LKW hinzufügen
def lkw_hinzufuegen():
    with open("flotten_datenbank.json", "r") as f:
        flotte = json.load(f)
    print("\n--- NEUEN LKW REGISTRIEREN ---")
    neue_id = input("Neue LKW-ID (z.B. HH-04): ")
    neue_person = hole_sauberen_namen()
    neue_last = int(input("Ladung in kg: "))

    neuer_lkw = {"ID": neue_id, "Fahrer_in": neue_person, "Last": neue_last}
    flotte.append(neuer_lkw)
    with open("flotten_datenbank.json", "w") as f:
        json.dump(flotte, f, indent=4)
    print(f"✅️ {neue_person} wurde registriert!")

# Option 3: LKW löschen
def lkw_loeschen():
    with open("flotten_datenbank.json", "r") as f:
        flotte = json.load(f)
    print("\n--- LKW AUSMUSTERN (LÖSCHEN) ---")
    ziel_id = input("Welche LKW-ID soll gelöscht werden?: ")

    gefunden = False
    for lkw in flotte:
        if lkw["ID"] == ziel_id:
            flotte.remove(lkw)
            gefunden = True
            break

    if gefunden:
        with open("flotten_datenbank.json", "w") as f:
            json.dump(flotte, f, indent=4)
        print(f"✅️ Erfolg: LKW {ziel_id} wurde gelöscht.")
    else:
        print(f"⚠️ ID {ziel_id} nicht gefunden.")

# --- HAUPTSCHLEIFE ---
while True:
    print("\n==============================")
    print("--- SPEDITIONN HAMBURG V5 ---")
    print("==============================")
    print("1: Flotte anzeigen")
    print("2: Neuen LKW registrieren")
    print("3: LKW ausmustern (Löschen)")
    print("4: Beenden")

    auswahl = input("\nDeine Auswahl: ")
    if auswahl == "1":
        zeige_flotte()
    elif auswahl == "2":
        lkw_hinzufuegen()
    elif auswahl == "3":
        lkw_loeschen()
    elif auswahl == "4":
        print("System wird sicher heruntergefahren. Tschüss, Valentin!")
        break
    else:
        print("❌️ Ungültige Auswahl!")
