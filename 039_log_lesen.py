# Liest die Logbuch-Datei aus und zeigt ihren Inhalt an, oder meldet wenn sie leer/fehlt

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
