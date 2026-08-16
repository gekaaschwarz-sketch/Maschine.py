import json

# Wächter 1: Namens-Schutz MIT NOTAUS-SYSTEM! 
def hole_sauberen_namen():
    while True:
        name = input("Name der Fahrer*in (oder 'zurueck' zum Abbrechen): ")

        # Das Notaus-Signal für den stressigen Logistik-Alltag:
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

# Option 2: LKW hinzufügen mit Abbruch-Logistik 
def lkw_hinzufuegen():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
    except FileNotFoundError:
        flotte = []

    print("\n--- NEUEN LKW REGISTRIEREN ---")
    neue_id = input("Neue LKW ID: ")

    # Hier holen wir den Namen oder das Abbruch-Signal
    neue_person = hole_sauberen_namen()

    # Das Notaus-Signal wird hier ausgewertet:
    if neue_person == "ABBRUCH":
        print("⚠️ Registrierung abgebrochem! Zurück zum Hauptmenü.")
        return # Funktion wird sofort beendet, bevor Daten gespeichert werden!

    last = int(input("Ladung in kg: "))
    flotte.append({"ID": neue_id, "Fahrer_in": neue_person, "Last": last})
    with open("flotten_datenbank.json", "w") as f:
        json.dump(flotte, f, indent=4)
    print(f"✅️ {neue_person} wurde erfolgreich registriert!")

# --- HAUPTSCHLEIFE ---
while True:
    print("\n==============================")
    print("--- SPEDITION HAMBURG V9 ---")
    print("==============================")
    print("1: Flotte anzeigen")
    print("2: Neu LKW registrieren")
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
