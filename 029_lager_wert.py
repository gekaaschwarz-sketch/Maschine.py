# 029_lager_wert.py

lager = {
    "Holz": 1500,
    "Stahl": 2500,
    "Glas": 800
}

# .values() holt nur die Zahlen aus dem Dictionary
alle_gewichte = lager.values()

gesamt_gewicht = sum(alle_gewichte)

print("--- LAGER-ANALYSE ---")
print("Anzahl der Positionen: " + str(len(lager)))
print("Gesamtgewicht im lager: " + str(gesamt_gewicht) + " kg")

# Kleiner Bonus: Durchschnittsgewicht pro Artikel
durchschnitt = gesamt_gewicht / len(lager)
print("Durchschnitt pro Artikel: " + str(round(durchschnitt, 2)) + " kg")
