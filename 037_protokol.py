# 037_protokoll.py
import datetime # Holt die aktuelle Uhrzeit

def log_schreiben(text):
    zeit = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    f = open("logbuch.txt", "a") # "a" steht für append (anhängen)
    f.write(zeit + " - " + text + "\n")
    f.close()

# Test
print("System startet...")
log_schreiben("LVP Berechnung durchgeführt.")
print("Eintrag in Logbuch gespeichert.")
