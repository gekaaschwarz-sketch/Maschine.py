# 036_lvp_profi.py

def zahl_eingabe(aufforderung):
    while True:
        try:
            wert = float(input(aufforderung))
            return wert # Gibt die korrekte Zahl zurück und beendet die Schleife
        except ValueError:
            print("❌️ Fehler: Bitte nur Zahlen (z.B. 2500 oder 1.5) eingeben!")

# Das Hauptprogramm
print("--- PROFI LVP CHECK ---")
radstand = 5.5

# Wirnutzen unsere Sicherheits-Funktion für Gewicht UND Abstand
gewicht = zahl_eingabe("Gewicht der Ladung (kg): ")
abstand = zahl_eingabe("Abstand von vorn (m): ")

last_hinten = (gewicht * abstand) / radstand
print("-----------------------")
print("Hinterachslast: " + str(round(last_hinten, 2)) + " kg")
