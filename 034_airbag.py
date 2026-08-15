# Fragt ein Gewicht ab und faengt ungueltige (nicht-numerische) Eingaben per try/except ab

def sichere_eingabe():
    print("--- SICHERER GEWICHTS-CHECK ---")

    try:
        gewicht = int(input("Bitte Gewicht in kg eingeben: "))
        print("Erfolg: Das System hat " + str(gewicht) + " kg registriert.")

    except ValueError:
        print("❌️ FEHLER: Bitte nur Zahlen eingeben! Keine Buchstaben.")

# Start
sichere_eingabe()
