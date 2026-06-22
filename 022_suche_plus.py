# 022_suche_plus.py
fracht = ["Holz", "Stahl", "Papier", "Glas"]

def detail_suche(liste, gesuchter_artikel):
    print("--- Suche läuft ---")
    if gesuchter_artikel in liste:
        platz = liste.index(gesuchter_artikel)
        print("Erfolg! '" + gesuchter_artikel + "' gefunden.")
        print("Position in LKW: " + str(platz))
    else:
        print("Fehler: '" + gesuchter_artikel + "' ist nicht geladen.")

# Test
artikel = input("Was suchen Sie? ")
detail_suche(fracht, artikel)
