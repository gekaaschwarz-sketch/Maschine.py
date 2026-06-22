import json

# Wächter: Namens-Validierung
def hole_sauberen_namen():
    while True:
        name = input("Name der Fahrer*in: ")
        if name.isalpha():
            return name
        else:
            print("❌️ Fehler: Nur Buchstaben erlaubt!")

def zeige_flotte():
    with open("flotten_datenbank.json", "r") as f:
        flotte = json.load(f)
    print("\n--- 🚛️ AKTUELLE FLOTTE ---")
    for lkw in flotte:
        print(f"ID: {lkw['ID']} | Fahrer*in: {lkw['Fahrer_in']} | Last: {lkw['Last']} kg")

def lkw_hinzufuegen():
    with open("flotten_datenbank.json", "r") as f:
        flotte = json.load(f)

    print("\n--- NEUEN LKW REGISTRIEREN ---")
    neue_id = input("Neue LKW-ID (z.B. HH-03): ")
    neue_person = hole_sauberen_namen() # HIER WIRKT DER SCHUTZ!
    neue_last = int(input("Ladung in kg: "))

    neuer_lkw = {"ID": neue_id, "Fahrer_in": neue_person, "Last": neue_last}
    flotte.append(neuer_lkw)

    with open("flotten_datenbank.json", "w") as f:
        json.dump(flotte, f, indent=4)
    print(f"✅️ {neue_person} wurde erfolgreich registriert!")

# --- HAUPTSCHLEIFE ---
while True:
    print("\n--- SPEDITION HAMBURG TERM V4 ---")
    print("1: Flotte anzeigen")
    print("3: Neuen LKW registrieren")
    print("4: Beenden")

    auswahl = input("\nAuswahl: ")

    if auswahl == "1":
        zeige_flotte()
    elif auswahl == "3":
        lkw_hinzufuegen()
    elif auswahl == "4":
        print("System wird heruntergefahren. Tschüss, Valentin!")
        break
    else:
        print("❌️ Ungültige Auswahl!")
