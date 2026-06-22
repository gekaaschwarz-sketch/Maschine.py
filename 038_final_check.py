import datetime

# 1. Sicherheits-Eingabe
def zahl_eingabe(aufforderung):
    while True:
        try:
            wert = float(input(aufforderung))
            return wert # Gibt die korrekte Zahl zurück und beendet die Schleife
        except ValueError:
            print("❌️ Fehler: Bitte nur Zahlen eingeben!")

# 2. Long-Funktion
def log_schreiben(text):
    zeit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    f = open("logbuch.txt", "a")
    f.write(zeit + " - " + text + "\n")
    f.close()

# 3. Hauptprogramm
radstand = 5.5
print("--- LKW-PROFI-CHECK MIT PROTOKOLL ---")

gewicht = zahl_eingabe("Gewicht (kg): ")
abstand = zahl_eingabe("Abstand (m): ")

last = round((gewicht * abstand) / radstand, 2)
ergebnis_text = "Last: " + str(last) + " kg bei " + str(gewicht) + " kg Ladung."

print("ERGEBNIS: " + ergebnis_text)

# Speichern im Logbuch
log_schreiben(ergebnis_text)
print("✅️ Protokoll wurde aktualisiert.")
