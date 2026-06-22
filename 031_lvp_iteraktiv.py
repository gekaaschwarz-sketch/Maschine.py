# 031_lvp_iteraktiv.py

radstand = 5.5 # Fester Wert für deinem LKW

def check_achslast():
    print("--- LVP SCHNEL-CHECK ---")
    gewicht = int(input("Gewicht der Ladung (kg): "))
    abstand = float(input("Abstand von der Stirnwand (m): "))

    # Die Formel
    last_hinten = (gewicht * abstand) / radstand

    print("-------------------------")
    print("Zusätzliche Last auf Hinterachse: " + str(round(last_hinten, 2)) + " kg")

# Start
check_achslast()
