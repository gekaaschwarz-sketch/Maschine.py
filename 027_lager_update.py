# 027_lager_update.py

lager = {
    "Holz": 1500,
    "Stahl": 2500
}

print("Lager vor dem Update: " + str(lager))

# Ein neues Gut hinzufügen
neu_gut = input("Welches neue Gut wird geladen? ")
neu_gewicht = int(input("Wie viel kg wiegt es? "))

# Hier passiert das Update:
lager[neu_gut] = neu_gewicht

print("Lager nach dem Update: " + str(lager))
