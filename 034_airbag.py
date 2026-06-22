# 034_airbag.py

def sichere_eingabe():
    print("--- SICHERER GEWICHTS-CHECK ---")

    try:
        gewicht = int(input("Bitte Gewicht in kg eingeben: "))
        print("Erfolg: Das System hat " + str(gewicht) + " kg registriert.")

    except ValueError:
        print("❌️ FEHLER: Bitte nur Zahlen eingeben! Keine Buchstaben.")

# Start
sichere_eingabe()
