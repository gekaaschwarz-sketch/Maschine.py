# 016_suche.py

def fracht_suchen(liste, gesuchter_artikel):
    if gesuchter_artikel in liste:
        # .index() sagt uns die Position (0,1, 2...)
        platz = liste.index(gesuchter_artikel)
        print("Gefunden! '" + gesuchter_artikel + "' liger auf Platz " + str(platz))
    else:
        print("Leider nicht an Bord: " + gesuchter_artikel)

# Test-LKW
lkw_ladung = ["Holz", "Stahl", "Papier", "Glas"]

print("--- Ladungskontrolle ---")
suchbegriff = input("Welches Gut suchen Sie? ")
fracht_suchen(lkw_ladung, suchbegriff)
