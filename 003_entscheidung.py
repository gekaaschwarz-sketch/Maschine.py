# 003_entscheidung.py
print("--- Rechnen-Wahl ---")
wahl = input("Willst du (P)lus oder (M)inus rechnen? ")
z1 = int(input("Zahl 1: "))
z2 = int(input("Zahl 2: "))
if wahl == "P":
    print("Ergebnis der Addition: " + str(z1 + z2))
if wahl == "M":
    print("Ergebnis der Subtraktion: " + str(z1 - z2))
