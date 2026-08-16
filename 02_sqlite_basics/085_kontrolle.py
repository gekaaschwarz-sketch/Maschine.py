import sqlite3

print("\n=========================================")
print("--- FINALER SQL-TRESOR CHECK ---")
print("=========================================")

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("SELECT * FROM lkw_flotte")
alle_lkw = cursor.fetchall()

for zeile in alle_lkw:
    print(f"🚛 LKW: {zeile[0]} | Crew: {zeile[1]} | Aktuelle Last: {zeile[2]} kg")

verbindung.close()