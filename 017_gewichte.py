# 017_gewichte.py

# Zwei Listen, die zusammengehören
fracht = ["Holz", "Stahl", "Papier"]
gewichte = [500, 2500, 150] # Gewicht in kg

def gewicht_prüfen(artikel_liste, gewicht_liste, gesuchter_artikel):
    if gesuchter_artikel in artikel_liste:
        # 1. Wo ligt der Artikel?
        index = artikel_liste.index(gesuchter_artikel)
        #2. Hoie des Gewicht an der gleichen Stelle
        gewicht = gewicht_liste[index]
        print("Gefunden! '" + gesuchter_artikel + "' wiegt " + str(gewicht) + " kg.")
    else:
        print("Artikel nicht auf der Ladeliste.")

print("--- Gewichtskontrolle ---")
suche = input("Welches Gut wigen? ")
gewicht_prüfen(fracht, gewichte, suche)
