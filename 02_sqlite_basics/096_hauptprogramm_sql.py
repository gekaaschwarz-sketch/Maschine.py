# Erstes SQL-Hauptmenue: zeigt die Flotte aus der Datenbank an, nur Anzeigen und Beenden moeglich
import sqlite3

DB_TABLE_LKW = "fleet_trucks"  # zentral konfigurierbarer Tabellenname für LKWs

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

        cursor.execute(f"SELECT * FROM {DB_TABLE_LKW}")
        alle_lkw = cursor.fetchall()

        print("\n--- 🗄️ SQL-TRESOR: AKTUELLE FLOTTE ---")
        for zeile in alle_lkw:
            print(f"ID: {zeile[0]} | Fahrer_in: {zeile[1]} | Last: {zeile[2]} kg")

        verbindung.close()
    
    elif auswahl == "4":
        print("\nTschüss, Valentin! Sichere Fahrt!")
        break