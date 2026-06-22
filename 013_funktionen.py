# 013_funktionen.py

# Wir definieren eine Funktion (einen Baukasten)
def begrüßung(name):
    print("Hallo " + name + "!")
    print("Wilkommen in deiner Logistik-Software.")

# Hier rufen wir die Funktion auf
nutzer = input("Wie heißt du? ")
begrüßung(nutzer)
