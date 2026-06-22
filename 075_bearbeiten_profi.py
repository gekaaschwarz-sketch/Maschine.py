import json

# Option 1: Flotte anzeigen
def zeige_flotte():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
        print("\n--- 🚛️ AKTUELLE FLOTTE ---")
        for lkw in flotte:
            print(f"ID: {lkw['ID']} | Fahrer*in: { lkw['Fahrer_in']} | Last: {lkw['Last']} kg")
    except FileNotFoundError:
        print("❌️ Keine Datenbank gefunden.")

# Option 6: LADUNG EINES LKWS BEARBEITEN (NEU!)
def lkw_bearbeiten():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
    except FileNotFoundError:
        print("❌️ Keine Datenbank vorhanden.")
        return

    print("\n--- 📝️ LKW-LADUNG BEARBEITEN ---")
    such_id = input("Welche LKW-ID möchtest du bearbeiten? (oder 'zurueck'): ")

    if such_id.lower() == "zurueck":
        return

    # Wächter durchsucht die Liste nach der ID
    gefunden = False
    for lkw in flotte:
        if lkw["ID"] == such_id:
            print(f"\n✅️ LKW gefunden! Aktuelle Ladung von {lkw['Fahrer_in']}: {lkw['Last']} kg")

            # Neues Gewicht mit Try-Except-Schutz abfragen
            while True:
                eingabe = input("Gib das neue Gewicht ein (oder 'zurueck'): ")
                if eingabe.lower() == "zurueck":
                    return
                try:
                    neues_gewicht = int(eingabe)
                    if 0 <= neues_gewicht <= 40000:
                        lkw["Last"] = neues_gewicht # Wert wird im Speicher überschrieben!
                        gefunden = True
                        break
                    else:
                        print("❌️ Fehler: Gewicht unlogisch(0 bis 40.000 kg)!")
                except ValueError:
                    print("❌️ Fehler: Bitte nur ganze Zahlen eingeben!")
            break

    if gefunden:
        # Geänderte Liste sofort wieder aus der Crucial-SSD abspeichern
        with open("flotten_datenbank.json", "w") as f:
            json.dump(flotte, f, indent=4)
        print(f"📝️ Erfolg: Das Gewicht der ID '{such_id}' wurde erfolgreich aktualisiert")
    else:
        print(f"⚠️ WARNUNG: Die LKW-ID '{such_id}' existiert nicht im System!")

# --- HAUPTSCHLEIFE ---
while True:
    print("\n==============================")
    print("--- SPEDITION HAMBURG V15 ---")
    print("==============================")
    print("1: Flotte anzeigen")
    print("6: LKW-Ladung bearbeiten")
    print("4: Beenden")

    auswahl = input("\nDeine Auswahl: ")
    if auswahl == "1":
        zeige_flotte()
    elif auswahl == "6":
        lkw_bearbeiten()
    elif auswahl == "4":
        print("System wird sicher heruntergefahren. Tschüss, Valentin!")
        break
    else:
        print("❌️ Ungültige Auswahl")
