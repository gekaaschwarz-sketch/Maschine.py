# 039_log_lesen.py

def logbuch_anzeigen():
    print("--- DIGITALE LOGBUCH-AUSGABE ---")
    try:
        f = open("logbuch.txt", "r") # "r" steht für read (lesen)
        inhalt = f.read()
        f.close()

        if inhalt:
            print(inhalt)
        else:
            print("Das Logbuch ist noch leer.")

    except FileNotFoundError:
        print("❌️ Fehler: Keine Logbuch-Datei gefunden.")

# Start
logbuch_anzeigen()
