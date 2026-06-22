import sqlite3

while True:
    print("\n=========================================")
    print("--- 🚛 SPEDITION HAMBURG SQL ---")
    print("=========================================")
    print("1: Flotte anzeigen")
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
    
    elif auswahl == "4":
        print("\nTschüss, Valentin! Sichere Fahrt!")
        break