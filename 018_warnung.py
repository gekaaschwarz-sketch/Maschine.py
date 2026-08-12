# Prueft das Gewicht eines Gutes und warnt, wenn es die 1000-kg-Grenze
print("--- ⚠️ SICHERHEITS-CHECK: AUTOMATISCHE GEWICHTS-SCHWELLENWERT-WARNUNG ---")

fracht = ["Hol", "Stahl", "Papir"]
gewichte = [500, 2500, 150]

def fracht_check(artikel_liste, gewicht_liste, gesuchter_artikel):
    if gesuchter_artikel in artikel_liste:
        index = artikel_liste.index(gesuchter_artikel)
        gewicht = gewicht_liste[index]

        print("Artikel: " + gesuchter_artikel + "( " + str(gewicht) + " kg)")

        # Die Warn-Logik
        if gewicht > 1000:
            print("⚠️ WARNUNG: Dises Gut ist zu schwer für den Standart-LKW!")
        else:
            print("✅️ Status: Gewicht in normalen Bereich.")
    else:
        print("Fehler: Artikel nicht gefunden.")

suche = input("Welches Gut soll geprüft werden? ")
fracht_check(fracht, gewichte, suche)