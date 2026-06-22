def hole_zahl_im_bereich(name, minimum, maximum):
    while True:
        try:
            wert = float(input(name + " eingeben: "))
            if minimum <= wert <= maximum:
                return wert
            else:
                print("❌️ Fehler: Der Wert muss zwischen " + str(minimum) + " und " + str(maximum) + " liegen! ")
        except ValueError:
            print("❌️ Fehler: Bitte nur Zahlen eingeben!")

# Test für die LKW-Länge (zwischen 5m und 18.75)
laenge = hole_zahl_im_bereich("LKW-Länge", 5, 18.75)
print("Registrierte Länge: " + str(laenge) + " m ")
