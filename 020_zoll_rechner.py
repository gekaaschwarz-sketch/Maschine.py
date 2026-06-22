# 020_zoll_rechner.py
fracht = ["Holz", "Stahl", "Papier"]
gewichte = [1500, 2500, 150]
zoll_pro_kg = 0.15 # 15 Cent pro Kilo

def berechne_zoll(artikel_liste, gewicht_liste, steuer_satz):
    gesamt_gewicht = sum(gewicht_liste)
    gesamt_zoll = gesamt_gewicht * steuer_satz

    print("--- ZOLL-ABRECHNUNG ---")
    print("Gesamtgewicht: " + str(gesamt_gewicht) + " kg")
    print("Steuersatz: " + str(steuer_satz) + " EUR/kg")
    print("-----------------------")
    # rund(..., 2) rundet auf 2 Cent-Stellen
    print("GESAMTZOLL: " + str(round(gesamt_zoll, 2)) + "EUR")

# Funktion starten
berechne_zoll(fracht, gewichte, zoll_pro_kg)
