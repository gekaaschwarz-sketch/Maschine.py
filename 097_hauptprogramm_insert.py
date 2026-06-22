import sqlite3

while True:

    print("\n=====================================")
    print("--- 🚛 SPEDITION HAMBURG SQL ---")
    print("=====================================")
    print("1: Flotte anzeigen")
    print("2: LKW hinzufügen")
    print("4: Beenden")

    auswahl = input("\nDeine Auswahl: ")

    if auswahl == "1":
        verbindung = sqlite3.connect("speditions_tresor.db")
        cursor = verbindung.cursor()

        cursor.execute("SELECT * FROM lkw_flotte")
        alle_lkw = cursor.fetchall()

        print("\n--- 🗄️ SQL-TRESOR: AKTUELLE FLOTTE ---")
        for zeile in alle_lkw:
            print(f"ID: {zeile[0]} | Fahrer_in: {zeile[1]} | Last: {zeile[2]} kg")

        verbindung.close()

    elif auswahl == "2":
        print("\n--- 📥️ NEUEN LKW REGISTRIEREN ---")
        neue_id = input("Gib die neue LKW-ID ein: ")
        neuer_fahrer = input("Wer ist der Fahrer / die Fahrerin?: ")
        neue_last = int(input("Wie viele kg Last hat der LKW?: "))

        verbindung = sqlite3.connect("speditions_tresor.db")
        cursor = verbindung.cursor()

        cursor.execute("INSERT INTO lkw_flotte (id, fahrer_in, last) VALUES (?, ?, ?)", (neue_id, neuer_fahrer, neue_last))
        verbindung.commit() # Ganz wichtig bei Änderung!
        verbindung.close()

        print(f"✔️ LKW {neue_id} erfolgreich im SQL-Tresor verankert!")

    elif auswahl == "4":
        print("\nTschüss, Valentin! Sichere Fahrer!")
        break