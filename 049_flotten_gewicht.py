# 049_flotten_gewicht.py

flotte = [
    {"ID": "HH-01", "Fahrer_in": "Valentin", "Last": 2500},
    {"ID": "HH-02", "Fahrer_in": "Yvonne", "Last": 1200},
    {"ID": "HH-03", "Fahrer_in": "Stefan", "Last": 3800}
]

def gesamt_last_berechnen(lkw_liste):
    total = 0 # Wir starten bei Null

    for lkw in lkw_liste:
        total = total + lkw["Last"]

    print("--- FLOTTEN-ANALYSE ---")
    print("Gesamtgewicht aller LKW: " + str(total) + " kg")

# Start
gesamt_last_berechnen(flotte)
