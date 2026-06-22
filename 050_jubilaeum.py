# 050_jubilaeum.py

flotte = [
    {"ID": "HH-01", "Fahrer_in": "Valentin", "Last": 2500},
    {"ID": "HH-02", "Fahrer_in": "Yvonne", "Last": 1200},
    {"ID": "HH-03", "Fahrer_in": "Stefan", "Last": 3800}
]

def grosse_analyse(lkw_liste):
    anzahl = len(lkw_liste)
    total = sum(lkw['Last'] for lkw in lkw_liste)
    durchschnitt = total / anzahl

    # Den schwersten LKW finden
    schwerster = max(lkw_liste, key=lambda x: x['Last'])

    print("--- 🏆️ JUBILÄUM: FLOTEN-REPORT 050 ---")
    print("Anzahl LKW: " + str(total) + " kg")
    print("Durchschnittslast: " + str(round(durchschnitt, 2)) + " kg")
    print("---------------------------------------")
    print("⚠️ SCHWERSTER LKW: " + schwerster['ID'] + "(" + schwerster['Fahrer_in'] + ")")

# Start
grosse_analyse(flotte)
