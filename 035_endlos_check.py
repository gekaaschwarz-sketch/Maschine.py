# 035_endlos_check.py

def gewicht_erzwingen():
    while True: # Die Schleife läuft ewig...
        try:
            gewicht = int(input("Bitte Gewicht eingeben (nur Zahlen): "))
            print("✅️ Perfekt! " + str(gewicht) + " kg gespeichert.")
            break # ...bis hier das 'break' die Schleife stoppt!

        except ValueError:
            print("❌️ Fehler! Das war keine Zahl. Nochmal versuchen...")

# Start
gewicht_erzwingen()
