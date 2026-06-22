def hole_positives_gewicht():
    while True:
        try:
            gewicht = float(input("Gewicht eingeben (kg): "))
            if gewicht <= 0:
                print("❌️ Fehler: Ein LKW kann keine negativen Lasten tragen!")
            else:
                return gewicht
        except ValueError:
            print("❌️ Fehler: Bitte: nur Zahlen eingeben")

# Test
print("System bereit für Sicherheits-Check...")
mein_gewicht = hole_positives_gewicht()
print("Registriert: " + str(mein_gewicht) + " kg")
