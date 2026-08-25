# Erweitert das SQL-Hauptmenue um das Loeschen eines LKW per ID (mit Abbruch-Option 'x')
import sqlite3

# Konfiguration: zentrale Konstanten für DB-Pfad und Tabellennamen
DB_PATH = "speditions_tresor.db"
DB_TABLE_LKW = "fleet_trucks"  # setze hier den tatsächlichen Tabellennamen

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
        verbindung = sqlite3.connect(DB_PATH)
        cursor = verbindung.cursor()

        cursor.execute(f"SELECT * FROM {DB_TABLE_LKW}")
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

        verbindung = sqlite3.connect(DB_PATH)
        cursor = verbindung.cursor()

        cursor.execute(f"INSERT INTO {DB_TABLE_LKW} (id, fahrer_in, last) VALUES (?, ?, ?)",
                       (neue_id, neuer_fahrer, neue_last))
        verbindung.commit()
        verbindung.close()

        print(f"✔️ LKW {neue_id} erfolgreich im SQL-Tresor verankert!")
    
    elif auswahl == "3":
        print("\n--- 🗑️ LKW-ID AUS TRESOR LÖSCHEN ---")
        print("(Tippe 'X' ein, um den Vorgang abzubrechen)") # 💡 Hinweis für den Disponenten
        loesch_id = input("Welche LKW-ID soll gelöscht werden? (z.B. HH-06): ")

        # --- DER NEUE SCHUTZWALL (REPARATUR!) ---
        if loesch_id.lower() == "x":
            print("\n❌ Löschvorgang abgebrochen. Zurück zum Hauptmenü!")
            continue  # 💡 Das 'continue' springt sofort an den Anfang der while-Schleife zurück!

        # Erst wenn der Schutzwall überwunden ist, öffnen wir die Datenbank!
        verbindung = sqlite3.connect(DB_PATH)
        cursor = verbindung.cursor()

        cursor.execute(f"DELETE FROM {DB_TABLE_LKW} WHERE id = ?", (loesch_id,))
        verbindung.commit()
        verbindung.close()

        print(f"\n🗑️ LKW {loesch_id} wurde erfolgreich aus dem SQL-Tresor entfernt!")

    elif auswahl == "4":
        print("\nTschüss, Valentin! Sichere Fahrt!")
        break