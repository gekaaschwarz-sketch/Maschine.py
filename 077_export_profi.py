import json

# Option 1: Flotte anzeigen
def zeige_flotte():
    try:
        with open("flotten_datenbank.json" ,"r") as f:
            flotte = json.load(f)
            print("\n--- 🚛 AKTUELLE FLOTTE ---")
            for lkw in flotte:
                print(f"ID: {lkw['ID']} | Fahrer*in: {lkw['Fahrer_in']} | Last: {lkw['Last']} kg")
    except FileNotFoundError:
        print("❌ Keine Datenbank gefunden.")

# Option 8: DATEN EXPORTIEREN IN EINE TEXTDATEI (NEU!)
def flotte_exportieren():
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)
    except FileNotFoundError:
        print("❌ Keine Daten zum Exportieren vorhanden.")
        return
    
    print("\n--- 💾 FLOTTEN-EXPORT STARTEN ---")
    dateiname = "speditions_bericht.txt"

    # Wir öffnen eine NEUE Textdatei zum Schreiben ("w")
    with open(dateiname, "w") as f:
        f.write("=========================================\n")
        f.write("   OFFIZIELER BERICHT: SPEDITION HAMBURG\n")
        f.write("=========================================\n\n")

        for lkw in flotte:
            f.write(f"🚛 LKW-ID: {lkw['ID']}\n")
            f.write(f"👤 Fahrer*in: {lkw['Fahrer_in']}\n")
            f.write(f"⚖️ Aktuelle Last: {lkw['Last']} kg\n")
            f.write("-----------------------------------------\n")

    print(f"✅ Erfolg: Bericht wurde sicher unter '{dateiname}' gespeichert!")

# --- HAUPTSCHLEIFE ---
while True:
    print("\n==============================")
    print("--- SPEDITION HAMBURG V17 ---")
    print("==============================")
    print("1: Flotte anzeigen")
    print("8: Bericht als Textdatei exportieren")
    print("4: Beenden")

    auswahl = input("\nDeine Auswahl: ")
    if auswahl == "1":
        zeige_flotte()
    elif auswahl == "8":
        flotte_exportieren()
    elif auswahl == "4":
        print("System wird sicher herunterfahren. Tschüss, Valentin!")
        break
    else:
        print("❌ Ungültige Auswahl")
