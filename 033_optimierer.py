# 033_optimierer.py

radstand = 5.5
max_achslast = 6000

def optimierung():
    print("--- POSITIONS-OPTIMIERER ---")
    gewicht = int(input("Gewicht der Ladung (kg): "))

    # Formel für den maximalen Abstand:
    # Max_Abstand = (Max_Achslast * Radstand) / Gewicht
    max_abstand = (max_achslast * radstand) / gewicht

    print("----------------------------")
    if max_abstand > radstand:
        print("Ergebnis: Dieses Gewicht ist für den LKW völlig unbedenklich.")
    else:
        print("LÖSUNG: Das Gut darf MAXIMAL " + str(round(max_abstand, 2)) + " m von vorn stehen.")
        print("So halten Sie die 6000 kg Achslast genau ein.")

# Start
optimierung()
