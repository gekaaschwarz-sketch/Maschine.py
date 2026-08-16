import os

datei = "lager.txt"
fracht = []

# 1. AUTOMATISCH LADEN
if os.path.exists(datei):
    f = open(datei, "r")
    inhalt = f.read()
    if inhalt: # Nur wenn die Datei nicht leer ist
        fracht = inhalt.split(",") # Macht aus Text wieder eine Liste
    f.close

#2. HAUPTSCHLEIFE
while True:
    print("\nAktuelle: Fracht: " + str(fracht))
    wahl = input("Was tun? (a = hinzufügen, l = löschen, e = ende): ")

    if wahl == "e":
        # AUTOMATISCH SPEICHERN BEIM BEENDEN
        f = open(datei, "w")
        f.write(",".join(fracht)) # Macht aus der Liste wieder Text
        f.close()
        print("Gespeichert. Bis bald!")
        break

    if wahl == "a":
        neu = input("Was soll geladen werden? ")
        fracht.append(neu)

    if wahl == "l":
        raus = input("Was soll entladen werden")
        fracht.remove(raus)
