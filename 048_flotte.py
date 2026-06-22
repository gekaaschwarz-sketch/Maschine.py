# 048_flotte.py

# Eine Liste mit drei LKW-Datensätzen
flotte = [
    {"ID": "HH-01", "Fahrer_in": "Valentin", "Last": 2500},
    {"ID": "HH-02", "Fahrer_in": "Yvonne", "Last": 1200},
    {"ID": "HH-03", "Fahrer_in": "Stefan", "Last": 3800}
]

def status_bericht(lkw_liste):
    print("--- SPEDITION HAMBURG: STATUS ---")
    for lkw in lkw_liste:
        # Wir ziehen die Daten aus jedem einzelnen Dictionary
        print("LKW: " + lkw["ID"] + "| Fahrer*in: " + lkw["Fahrer_in"])

# Start
status_bericht(flotte)
