# Funktion 1: Namens-Check
def hole_namen():
    while True:
        name = input("Name der Fahrer*in: ")
        if name.isalpha():
            return name
        else:
            print("❌️ Fehler: Nur Buchstaben erlaubt!")

# Funktion 2: Last-Ceck
def hole_last():
    while True:
        try:
            last = int(input("Ladung in kg (0-40000): "))
            if 0 <= last <= 40000:
                return last
            else:
                print("❌️ Fehler: Gewicht unlogisch!")
        except ValueError:
            print("❌️ Fehler: Nur Zahlen erlaubt!")

# Hauptteil
print("--- DATEN-VALIDIERUNG LVP ---")
name = hole_namen()
gewicht = hole_last()

print(f"✅️ Datensatz geprüft: {name} mit {gewicht} kg. Bereit zum Speichern.")
