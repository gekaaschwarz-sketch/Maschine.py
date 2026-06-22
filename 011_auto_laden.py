import os # Das ist ein Werkzeugkasten für dein Betriebssystem

datei_name = "lager.txt"

# Prüfen, ob die Datei überhaupt existiert
if os.path.exists(datei_name):
    print("Gedächtnis wird geladen...")
    f = open(datei_name, "r")
    inhalt = f.read()
    f.close()
    print("Geladene Fracht: " + inhalt)
else:
    print("Kein Gedächtnis gefunden. Starte mit leerem Lager.")

print("Maschine ist bereit.")
