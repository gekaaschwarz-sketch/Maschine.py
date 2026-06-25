import sqlite3

print("\n=========================================")
print("--- ⚡️ SQL-HOCHGESCHWINDIGKEITS-CHECK ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()
    cursor.execute("SELECT * FROM kunden")
    alle_kunden = cursor.fetchall()

    print("\n👥 Aktuelle Kundenliste in Schnellzugriff:")
    for kunde in alle_kunden:
        print(f"Kunden-ID: {kunde[0]} | Name: {kunde[1]} | LKW-ID: {kunde[2]}")