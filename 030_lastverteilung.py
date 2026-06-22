# 030_lastverteilung.py

# Daten: [Gewicht_kg, Abstand_von_vorn_meter]
lager = {
    "Maschine_A": [2000, 1.5],
    "Maschine_B": [1500, 4.0]
}

radstand = 5.5 # Meter zwischen den Achsen

def achslast_berechnen(datenbank, radstand_lkw):
    print("--- LASTVERTEILUNG-ANALYSE ---")
    gesamt_hinterachse = 0

    for name, werte in datenbank.items():
        gewicht = werte[0]
        abstand = werte[1]

        # Formel für die Last auf der Hinterachse:
        # Last_Hinter = (Gewicht * Abstand) / Randstand
        anteil_hinten = (gewicht * abstand) / radstand_lkw
        gesamt_hinterachse += anteil_hinten

        print(name + ": drück mit " + str(round(anteil_hinten, 2)) + "kg auf die Hinterachse.")

    print("-------------------------------")
    print("Gesamtlast Hinterachse: " + str(round(gesamt_hinterachse, 2)) + " kg")

# Start
achslast_berechnen(lager, radstand)
