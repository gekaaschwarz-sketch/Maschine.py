import sqlite3

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("SELECT * FROM lkw_flotte")
alle_lkw = cursor.fetchall()

print("\n--- 🗄️ SQL-DATENBANK: AKTUELLE FLOTTE ---")
for zeile in alle_lkw:
    print(f"ID: {zeile[0]} | Fahrer*in: {zeile[1]} | Last: {zeile[2]} kg")

verbindung.close()