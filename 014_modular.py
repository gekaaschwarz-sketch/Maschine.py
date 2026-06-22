# 014_modular.py

# 1. Funktion definieren
def zeige_status(liste):
    print("\n--- LKW-STATUS ---")
    if len(liste) == 0:
        print("Der LKW ist leer.")
    else:
        print("Geladene Güter: " + str(liste))
    print("------------------\n")

# 2. Das Programm nutzen
meine_fracht = ["Computer", "Monitore"]

# Hier rufen wir die Funktionen auf
zeige_status(meine_fracht)

# Wir fügen etwas hinzu und rufen sie nochmal auf
meine_fracht.append("Transport")
zeige_status(meine_fracht)
