# 028_lager_loeschen.py

lager = {
    "Holz": 1500,
    "Stahl": 2500,
    "Glas": 800
}

print("Lager aktuell: " + str(lager))

# Ein Gut gezielt löschen
raus = input("Welches Gut wurde entladen? ")

if raus in lager:
    del lager[raus] # Der Befehl zum Löschen
    print("Erfolg: " + raus + " wurde aus dem System entfernt.")
else:
    print("Fehler: " + raus + " ist nicht im Lager.")

print("Lager nach dem Entladen: " + str(lager))
