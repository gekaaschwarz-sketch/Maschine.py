# 009_liste_loeschen.py
fracht = ['Holz', 'Stahl', 'Papier']
print('Aktuelle Fracht: ' + str(fracht))

# Den Nutyer fragen, was geöscht werden soll
raus = input('Welches Gut soll entladen werden? ')

# Das Element entfernen
if raus in fracht:
    fracht.remove(raus)
    print('Erfolgreich entladen.')
else:
    print('Dieses Gut ist nicht auf dem LKW!')

print('Restliche Fracht: ' + str(fracht))
