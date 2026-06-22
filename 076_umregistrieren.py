import json

# Option 1: Flotte anzeigen
def zeige_flotte():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
        print("\n--- 🚛 AKTUELLE FLOTTE ---")
        for lkw in flotte:
            print(f"ID: {lkw['ID']} | Fahrer*in: {lkw['Fahrer_in']} | Last: {lkw['Last']} kg")
    except FileNotFoundError:
        print("❌ Keine Datenbank gefunden.")

# Option 7: LKW VOLLSTÄNDIG UMREGISTRIEREN (NEU!)
def lkw_umregistrieren():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
    except FileNotFoundError:
        print("❌ Keine Datenbank vorhanden.")
        return

    print("\n--- 🔄 LKW UMREGISTRIEREN ---")
    such_id = input("Welche LKW-ID möchtest du komplett ändern? (oder 'zurueck'): ")

    if such_id.lower() == "zurueck":
        return

    gefunden = False
    for lkw in flotte:
        if lkw["ID"] == such_id:
            print(f"\n✅ LKW gefunden! Aktueller Fahrer: {lkw['Fahrer_in']}")

            # Neue Daten abfragen
            neue_id = input("Gib die NEUE LKW-ID ein: ")
            neuer_fahrer = input("Gib den NEUEN Fahrernamen ein: ")

            # Werte im Speicher überschreiben
            lkw["ID"] = neue_id
            lkw["Fahrer_in"] = neuer_fahrer
            gefunden = True
            break
        
    if gefunden:
        with open("flotten_datenbank.json", "w") as f:
            json.dump(flotte, f, indent=4)
        print("✅ Erfolg: LKW wurde erfolgreich umregistriert!")
    else:
        print(f"⚠️ WARNUNG: Die ID '{such_id}' existiert nicht!")

# --- HAUPTSCHLEIFE ---
while True:
    print("\n==============================")
    print("--- SPEDITION HAMBURG V16 ---")
    print("==============================")
    print("1: Flotte anzeigen")
    print("7: LKW umregistrieren")
    print("4: Beenden")

    auswahl = input("\nDeine Auswahl: ")
    if auswahl == "1":
        zeige_flotte()
    elif auswahl == "7":
        lkw_umregistrieren()
    elif auswahl == "4":
        print("System wird sicher herunterfahren. Tschüss, Valentin!")
        break
    else:
        print("❌ Ungültige Auswahl")
