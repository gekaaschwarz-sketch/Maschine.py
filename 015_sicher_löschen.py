# 015_sicher_löschen.py

def sicher_entladen(fracht_liste, artikel):
    print("ACHTUNG: Soll " + artikel + " wirklich gelöscht werden?")
    antwort = input("Tippe 'ja' zum Bestätigen: ")

    if antwort == "ja":
        fracht_liste.remove(artikel)
        print("Artikel wurde sicher entfernt.")
    else:
        print("Löschen abgebrochen.")

# Test-Daten
lager = ["Holz", "Stahl"]
sicher_entladen(lager, "Holz")
print("Aktueles Lager: " + str(lager))
