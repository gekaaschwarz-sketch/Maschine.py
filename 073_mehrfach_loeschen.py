import json

# Option 1: Flotte anzeigen
def zeige_flotte():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
        print("\n--- 🚛️ AKTUELLEN FLOTTE ---")
        for lkw in flotte:
            print(f"ID: {lkw['ID']} | Fahrer*in: {lkw['Fahrer_in']} | Last: {lkw['Last']} kg")
    except FileNotFoundError:
        print('❌️ Keine Datenbank gefunden.')

# Option 3: ALLE LKWs mit dieser ID löschen (VERSION V13!)
def lkw_loeschen_radikal():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
    except FileNotFoundError:
        print("❌️ Keine Datenbank vorhanden.")
        return

    print("\n--- 🗑️ RADIKALE MEhRFACH-LÖSCHUNG ---")
    loesch_id = input("Welche LKW-ID soll komplett entfernen werden? (oder 'zurueck'): ")

    if loesch_id.lower() == "zurueck":
        return

    # Wir zählen zuerst, wie oft die ID existiert
    anzahl_vorher = len(flotte)

    # DER HIGH-SPEED-FILTER: Behalten nur LKWs, die NICHT die loesch_id haben!
    flotte_neu = [lkw for lkw in flotte if lkw["ID"] != loesch_id]
    anzahl_nachher = len(flotte_neu)

    # Berechnung, wie viele Duplikate vernichtet wurden
    geloeschte_lkw = anzahl_vorher - anzahl_nachher

    if geloeschte_lkw > 0:
        # Sicherheits-Wächter fragt nach
        bestaetigung = input(f"⚠️ Wächter: Es wurden {geloeschte_lkw} Einträge mit der ID '{loesch_id}' gefunden. Alle löschen? (ja/nein): ")

        if bestaetigung.lower() == "ja":
            with open("flotten_datenbank.json", "w") as f:
                json.dump(flotte_neu, f, indent=4)
            print(f"🗑️ Erfolg: Alle {geloeschte_lkw} LKWs mit ID '{loesch_id}' wurden pulverisiert")
        else:
            print("❌️ Löschvorgang vom Chef abgebrochen.")
    else:
        print(f"❌️ Fehler: Keine LKWs mit der ID '{loesch_id}' in der Datenbank.")

# --- HAUPTSCHLEIFE ---
while True:
    print("\n==============================")
    print("--- SPEDITION HAMBURG V13 ---")
    print("==============================")
    print("1: Flotte anzeigen")
    print("3: LKW radikal löschen")
    print("4: Beenden")

    auswahl = input("\nDeine Auswahl: ")
    if auswahl == "1":
        zeige_flotte()
    elif auswahl == "3":
        lkw_loeschen_radikal()
    elif auswahl == "4":
        print("System wird sicher heruntergefahren. Tschüss, Valentin!")
        break
