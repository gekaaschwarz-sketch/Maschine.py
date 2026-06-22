import sqlite3

while True:
    print("\n=====================================")
    print("--- 🚛 SPEDITION HAMBURG SQL ---")
    print("=====================================")
    print("1: Flotte anzeigen")
    print("2: LKW hinzufügen")
    print("3: LKW löschen")
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
        verbindung.commit()
        verbindung.close()

        print(f"✔️ LKW {neue_id} erfolgreich im SQL-Tresor verankelt!")
    
    elif auswahl == "3":
        print("\n--- 🗑️ LKW-ID AUS TRESOR LÖSCHEN ---")
        print("(Tippe 'X' ein, um den Vorgang abzubrechen)") # 💡 Hinweis für den Disponenten
        loesch_id = input("Welche LKW-ID soll gelöscht werden? (z.B. HH-06): ")

        # --- DER NEUE SCHUTZWALL (REPARATUR!) ---
        if loesch_id.lower() == "x":
            print("\n❌ Löschvorgang abgebrochen. Zurück zum Hauptmenü!")
            continue  # 💡 Das 'continue' springt sofort an den Anfang der while-Schleife zurück!

        # Erst wenn der Schutzwall überwunden ist, öffnen wir die Datenbank!
        verbindung = sqlite3.connect("speditions_tresor.db")
        cursor = verbindung.cursor()

        cursor.execute("DELETE FROM lkw_flotte WHERE id = ?", (loesch_id,))
        verbindung.commit()
        verbindung.close()

        print(f"\n🗑️ LKW {loesch_id} wurde erfolgreich aus dem SQL-Tresor entfernt!")

    elif auswahl == "4":
        print("\nTschüss, Valentin! Sichere Fahrt!")
        break