# 025_benutzerfrundlich.py
fracht = ["Holz", "Stahl", "Papier"]

def smart_leeren(liste):
    print("!!! ACHTUNG: LKW leeren? !!!")
    antwort = input("Bestätigen mit 'ja': ")

    # .upper() macht aus 'ja', 'Ja' oder 'jA' immer 'JA'
    if antwort.upper() == "JA":
        liste.clear()
        print("Erfolg: Alles entladen.")
    else:
        print("Abbruch: Nichts passiert.")

# Test
smart_leeren(fracht)
print("Aktuelle Fracht: " + str(fracht))
