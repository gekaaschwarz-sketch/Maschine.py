# 004_logistik_tool.py
print("--- Logistik-Tool: Pfund in KG umrechnen ---")

# Abfrage
eingabe = input("Gewicht in Pfund (lb) eingeben: ")

# Umrechnung (float macht aus Text eine Kommazahl)
# 1 lb = 0.453592 kg
kg = float(eingabe) * 0.453592

# Ergebnis zeigen (auf 2 Stellen gerundet)
print("Das Ergebnis ist: " + str(round(kg, 2)) + " kg")
