# 008_fracht_manager.py
print("--- Interaktive Frachtliste ---")
meine_fracht = [] # Eine leere Liste zum Start

while True:
    artikel = input("Was soll geladen werden? (oder 'fertig' zum Beenden): ")
    
    if artikel == "fertig":
        break
    
    meine_fracht.append(artikel)
    print("Aktuelle Liste: " + str(meine_fracht))

print("--- Beladung abgeschlossen! ---")
print("Deine finale Ladeliste: " + str(meine_fracht))
