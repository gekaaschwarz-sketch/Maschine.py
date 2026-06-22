import json

def hole_validierte_last():
    while True:
        try:
            # try fängt ab, wenn der Nutzer Buchstaben statt Zahlen eintippt
            last = int(input("Ladung in kg (0-40000): "))
            if 0 <= last <= 40000:
                return last
            else:
                print("❌️ Fehler: Gewicht unlogisch (nur 0 bis 40.000 kg)!")
        except ValueError:
            print("❌️ Fehler: Bitte nur ganze Zahl eingeben! Keine Buchstaben!")

# Testlauf
print("--- TESTSTATION: GEWICHTS-WÄCHTER ---")
gepruefte_last = hole_validierte_last()
print(f"✅️ Erfolg: {gepruefte_last} kg im System blockiert.")
