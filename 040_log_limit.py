# 040_log_limit.py

def letzte_einträge_zeigen():
    print("--- NEUESTE LOG-EINTRÄGE ---")
    try:
        f = open("logbuch.txt", "r")
        # .readlines() macht aus jeder Zeile ein Listen-Element
        alle_zeilen = f.readlines()
        f.close()

        # Zeige nur die letzten 3 Einträge [-3:]
        letzte_drei = alle_zeilen[-3:]

        for zeile in letzte_drei:
            print(zeile.strip()) # .strip() entfernt die Leerzeichen

    except FileNotFoundError:
        print("Datei nicht gefunden.")

# Start
letzte_einträge_zeigen()
