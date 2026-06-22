def hole_validierte_last():
    while True:
        try:
            last = int(input("Ladung in kg (0 - 40000): "))
            if 0 <= last <= 40000:
                return last
            else:
                print("❌️ Fehler: Gewicht muss zwischen 0 und 40.000 kg ligen!")
        except ValueError:
            print("❌️ Fehler: Bitte nur ganze Zahlen eingeben!")

# Testlauf
print("--- SICHERHEITS-CHECK: LADUNG ---")
gepruefte_last = hole_validierte_last()
print(f"✅️ Erfolg: {gepruefte_last} kg registriert.")
