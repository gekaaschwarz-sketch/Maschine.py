# 032_lvp_warnung.py

radstand = 5.5
max_achslast = 6000 # Limit in kg

def check_achslast():
    print("--- LVP SICHERHEITS-CHECK ---")
    gewicht = int(input("Gewicht (kg): "))
    abstand = float(input("Abstand (m): "))

    last_hinten = (gewicht * abstand) / radstand

    print("-----------------------------")
    print("Berechnete Last: " + str(round(last_hinten, 2)) + " kg")

    # Die Warn-Logik
    if last_hinten > max_achslast:
        print("⚠️ ACHTUNG: Achslast überschritten! Umpositionieren!")
    else:
        print("✅️ Status: Achslast im grünen Bereich.")

check_achslast()
