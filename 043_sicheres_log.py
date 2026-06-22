import datetime

def hole_zahl_im_bereich(name, minimum, maximum):
    while True:
        try:
            wert = float(input(name + " eingeben: "))
            if minimum <= wert <= maximum:
                return wert
            else:
                print("❌️ Fehler: Wert außerhalb des Bereis")
        except ValueError:
            print("❌️ Fehler: Bitte nur Zahlen eingeben!")

# Die Speicher-Funktion
def log_schreiben(text):
    zeit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    f = open("logbuch.txt", "a")
    f.write(zeit + " - " + "\n")
    f.close()

# --- Hauptprogramm ---
print("--- SICHERE DATEN-ERFASSUNG ---")

# Wir prüfen die Achslast (darf z.B. nicht über 11500 sein)
achslast = hole_zahl_im_bereich("Achslast hinter (kg)", 0, 11500)

# Nur wenn die Prüfung bestaanden ist, wird geloggt
eintrag = "Geprpüfte Achslast: " + str(achslast) + "kg"
log_schreiben(eintrag)

print("✅️ Daten erfolgreich geprüft und in Logbuch gespeichert.")
