# 005_fehlerschutz.py
print("--- Sicherer Umrechner ---")
eingabe = input("Gewicht in Pfund eingeben: ")

try:
    # Versuche, die Eingabe in eine Zahl umzuwandeln
    kg = float(eingabe) * 0.453592
    print("Ergebnis: " + str(round(kg, 2)) + " kg")
except:
    # Falls oben ein Fehler passiert (z.B. Text statt Zahl)
    print("FEHLER: Bitte nur Zahlen eingeben (Nutze den Punkt statt Komma)!")

print("Programm beendet.")
