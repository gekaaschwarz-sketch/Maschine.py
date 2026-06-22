# 026_woerterbuch.py

# Ein Dictionary nutzt geschweifte Klammer { }
lager = {
    "Holz": 1500,
    "Stahl": 2500,
    "Papier": 150
}

def preis_abfrage(datenbank, gesuchter_artikel):
    if gesuchter_artikel in datenbank:
        gewicht = datenbank[gesuchter_artikel]
        print("Gefunden! " + gesuchter_artikel + " wiege " + str(gewicht) + " kg.")
    else:
        print("Artikel nicht im Verzeichnis.")

# Test
artikel = input("Welches Gut suchen Sie? ")
preis_abfrage(lager, artikel)
