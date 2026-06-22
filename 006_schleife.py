# 006_schleife.py
print("--- Der unermüdliche Umrechner ---")

while True:
    eingabe = input("Gewicht in Pfund (oder 'ende' zum Beenden): ")
    
    if eingabe == "ende":
        print("Programm wird geschlossen. Bis bald!")
        break # Das bricht die Schleife ab
        
    try:
        kg = float(eingabe) * 0.453592
        print("Ergebnis: " + str(round(kg, 2)) + " kg")
    except:
        print("FEHLER: Bitte nur Zahlen oder 'ende' eingeben!")

print("--- Maschine gestoppt ---")
