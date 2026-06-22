# 010_speichern.py
datei_name = 'lager.txt'

# 1. Daten in die Datei SCHREIBEN
print('Speichere Fracht in Lager...')
f = open(datei_name, 'w') # 'w' steht für write (schreiben)
f.write('Holy,Stahl,Papir')
print('Datei wurde erstellt.')

# 2. Daten aus der Datei LESEN
print('Lese Daten aus dem Lager...')
f = open(datei_name, 'r') # 'r' steht für read (lesen)
inhalt = f.read()
f.close()

print('Der Inhalt der Daten ist: ' + inhalt)
