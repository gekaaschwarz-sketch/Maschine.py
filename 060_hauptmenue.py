import json

def lade_flotte():
    with open("flotten_datenbank.json", "r") as f:
        return json.load(f)

def zeige_flotte():
    flotte = lade_flotte()
    print("\n--- 🚛️ AKTUELLE FLOTTE ---")
    for lkw in flotte:
        print(f"ID: {lkw['ID']} | Fahrer*in: {lkw['Fahrer_in']} | Last: {lkw['Last']} kg")

# --- HAUPTPROGRAMM ---
while True:
    print("\n==============================")
    print("--- SPEDITION HAMBURG TERM ---")
    print("==============================")
    print("1: Flote anzeigen")
    print("2: LKW ausmustern (Löschen)")
    print("4: Programm beenden")

    auswahl = input("\nDeine Auswahl: ")

    if auswahl == "1":
        zeige_flotte()
    elif auswahl == "2":
        print("\n[Funktion Löschen aufgerufen]")
        # Hir binden wir später deine Löschfunktion ein
    elif auswahl == "4":
        print("System wird sicher heruntergefahren. Tschüss, Valentin!")
        break
    else:
        print("❌️ Ungültige Auswahl! Bitte 1, 2 oder 4 wählen.")
