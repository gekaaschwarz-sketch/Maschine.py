import sqlite3

print("\n=========================================")
print("--- NEUEN LKW REGISTRIEREN ---")
print("=========================================")

neue_id = input("Gib die neue LKW-ID ein (z.B. HH-05): ")
neuer_fahrer = input("Wer ist der Fahrer / die Fahrerin?: ")
neue_last = int(input("Wie viel kg Last hat der LKW?: "))

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("INSERT INTO lkw_flotte (id, fahrer_in, last) VALUES (?, ?, ?)", (neue_id, neuer_fahrer, neue_last))

verbindung.commit()
verbindung.close()

print(f"🚛 LKW {neue_id} mit Fahrer*in {neuer_fahrer} wurde erfolgreich im Tresor verankert!")