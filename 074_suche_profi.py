import json

# Option 1: 
def zeige_flotte():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
        print("\n--- 🚛️ AKTUELLE FLOTTE ---")
        for lkw in flotte:
            print(f"ID: {lkw['ID']} | Fahrer*in: {lkw['Fahrer_in']} | Last: {lkw['Last']} kg")
    except FileNotFoundError:
        print("❌️ Keine Datenbank gefunden.")

# Option 5: LKW BLITZSCHNELL SUCHEN (NEU!)
def lkw_suchen():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
    except FileNotFoundError:
        print("❌️ Keine Datenbank vorhanden.")
        return

    print("\n--- 🔍️ LKW-SUCHE IM HAFEN ---")
    such_id = input("Welche LKW-ID suchst du? (oder 'zurueck'): ")

    if such_id.lower() == "zurueck":
        return

    # Der Wächter startet die Durchsuchen
    gefunden = False
    for lkw in flotte:
        if lkw["ID"] == such_id:
            print(f"\n✅️ LKW GEFUNDEN!")
            print(f"📍️ ID: {lkw['ID']} | Fahrer*in: {lkw['Fahrer_in']} | Ladung: {lkw['Last']} kg")
            gefunden = True
            break # Suche abbrechen, da Treffer gelandet!

    # Hier greift deine gewünschte Warnung, falls die ID nicht existirt:
    if not gefunden:
        print(f"⚠️ WARNUNG: Die LKW-ID '{such_id}' existiert nicht in System!")

# --- HAUPTSCHLEIFE ---
while True:
    print("\n==============================")
    print("--- SPEDITION HAMBURG V14 ---")
    print("==============================")
    print("1: Flotte anzeigen")
    print("5: LKW suchen per ID")
    print("4: Beenden")

    auswahl = input("\nDeine Auswahl: ")
    if auswahl == "1":
        zeige_flotte()
    elif auswahl == "5":
        lkw_suchen()
    elif auswahl == "4":
        print("System wird sicher heruntergefahren. Tschüss, Valentin!")
        break
