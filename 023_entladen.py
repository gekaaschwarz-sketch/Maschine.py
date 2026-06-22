# 023_entladen.py
fracht = ["Holz", "Stahl", "Papier", "Glas"]

def lkw_leeren(liste):
    print("LKW kommt in Hamburg an...")
    print("Aktuelle Ladung: " + str(liste))

    # Der magische Befehl zum Leeren
    liste.clear()

    print("Entladung abgeschlossen.")
    print("Ladung jetzt: " + str(liste))

# Funktion aufrufen
lkw_leeren(fracht)
