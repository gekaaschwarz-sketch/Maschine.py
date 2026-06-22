import json

# Option 1: Flotte anzeigen
def zeige_flotte():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
        print("\n--- 🚛 AKTUELLE FLOTTE ---")
        for lkw in flotte:
            print(f"ID: {lkw['ID']} | Fahrer*in {lkw['Fahrer_in']} | Last: {lkw['Last']} kg")
    except FileNotFoundError:
        print("❌ Keine Datenbank gefunden.")

# Option 9: STATISTIK-ZENTRALE BERECHNEN (NEU!)
def zeige_statistik():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
    except FileNotFoundError:
        print("❌ Keine Datenbank für Statistiken vorhanden.")
        return

    print("\n--- 📊 STATISTIK-ZENTRALE HAMBURG ---")
    anzahl_lkw = len(flotte)

    if anzahl_lkw == 0:
        print("⚠️ Das System ist leer. Keine Berechnungen möglich.")
        return

    # Wir brechen das gesamtgewicht über eine Schleife
    gesamt_gewicht = 0
    for lkw in flotte:
        gesamt_gewicht += lkw["Last"]

    # Mathematische Berechnung des Durchschnitts
    durchschnitt = gesamt_gewicht / anzahl_lkw

    print(f"🚛 Registrierte Fahrzeuge: {anzahl_lkw} LKW(s)")
    print(f"⚖️ Gesamtgewicht in Hafen : {gesamt_gewicht} kg")
    print(f"📊 Durchschnittliche Last : {durchschnitt:.2f} kg")

# --- HAUPTSCHLEIFE ---
while True:
    print("\n==============================")
    print("--- SPEDITION HAMBURG V18 ---")
    print("==============================")
    print("1: Flotte anzeigen")
    print("9: Statistik-Zentrale abrufen")
    print("4: Beenden")

    auswahl = input("\nDeine Auswahl: ")
    if auswahl == "1":
        zeige_flotte()
    elif auswahl == "9":
        zeige_statistik()
    elif auswahl == "4":
        print("System wird sicher herunterfahren. Tschüss, Valentin!")
        break
    else:
        print("❌ Ungültige Auswahl")