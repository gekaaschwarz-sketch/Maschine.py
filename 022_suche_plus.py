# Sucht ein Gut in der Fracht und gibt bei Erfolg zusaetzlich dessen Position aus
print("--- 🔎 POSITIONSSUCHE: DETAIL-RECHERCHE INNERHALB DER LKW-FRACHT ---")

fracht = ["Holz", "Stahl", "Papier", "Glas"]

def detail_suche(liste, gesuchter_artikel):
    if gesuchter_artikel in liste:
        platz = liste.index(gesuchter_artikel)
        print("Erfolg! '" + gesuchter_artikel + "' gefunden.")
        print("Position in LKW: " + str(platz))
    else:
        print("Fehler: '" + gesuchter_artikel + "' ist nicht geladen.")

# Test
artikel = input("Was suchen Sie? ")
detail_suche(fracht, artikel)