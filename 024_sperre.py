# 024_sperre.py
fracht = ["Holz", "Stahl", "Papier", "Glas"]

def sicheres_entladen(liste):
    print("!!! WARNUNG: Sie wollen den LKW komplett leeren !!!")
    bestätigung = input("Tippen Sie 'JA' zum Bestätigen: ")

    if bestätigung == "JA":
        liste.clear()
        print("Erfolg: LKW ist jetzt leer.")
    else:
        print("Abbruch: Ladung bleibt an Bord.")

# Test
sicheres_entladen(fracht)
print("Aktuelle Fracht: " + str(fracht))
