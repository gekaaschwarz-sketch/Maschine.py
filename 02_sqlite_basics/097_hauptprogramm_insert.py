# Erweitert das SQL-Hauptmenue um das Einfuegen eines neuen LKW in die Datenbank
import sqlite3

# Konfiguration: zentrale Konstanten für DB-Pfad und Tabellennamen
DB_PATH = "speditions_tresor.db"
DB_TABLE_LKW = "fleet_trucks"

while True:

    print("\n=====================================")
    print("--- 🚛 SPEDITION HAMBURG SQL ---")
    print("=====================================")
    print("1: Flotte anzeigen")
    print("2: LKW hinzufügen")
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

        cursor.execute(
            f"INSERT INTO {DB_TABLE_LKW} (id, fahrer_in, last) VALUES (?, ?, ?)",
            (neue_id, neuer_fahrer, neue_last)
        )
        verbindung.commit()
        verbindung.close()

        print(f"✔️ LKW {neue_id} erfolgreich im SQL-Tresor verankert!")

    elif auswahl == "4":
        print("\nTschüss, Valentin! Sichere Fahrer!")
        break
