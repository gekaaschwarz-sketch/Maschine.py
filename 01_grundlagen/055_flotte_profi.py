import json

# 1. Deine neue Sicherheits-Funktion
def hole_sauberen_namen():
    while True:
        name = input("Name der Fahrer*in: ")
        if name.isalpha():
            return name
        else:
            print("❌️ Fehler: Nur Buchstaben erlaubt!")

# 2. Das Hauptprogramm
def lkw_hinzufuegen():
    with open("flotten_datenbank.json", "r") as f:
        flotte = json.load(f)

    print("--- NEUEN LKW REGISTRIEREN ---")
    neue_id = input("LKW-ID (z.B. HH-05): ")

    # HIER NUTZEN WIR DIE SICHERHEIT:
    neue_person = hole_sauberen_namen()

    neue_last = int(input("Ladung (kg): "))

    neuer_lkw = {"ID": neue_id, "Fahrer_in": neue_person, "Last": neue_last}
    flotte.append(neuer_lkw)

    with open("flotten_datenbank.json", "w") as f:
        json.dump(flotte, f, indent=4)

    print(f"✅️ {neue_person} wurde sicher in der Datenbank gespeichert!")

# Start
lkw_hinzufuegen()
