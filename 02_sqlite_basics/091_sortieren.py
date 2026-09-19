import sqlite3

print("\n=========================================")
print("--- ⚖️ FLOTTE NACH GEWICHT SORTIERT ---")
print("=========================================")

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("SELECT * FROM fleet_trucks ORDER BY last DESC")
sortierte_lkw = cursor.fetchall()

for zeile in sortierte_lkw:
    print(f"🚛 LKW: {zeile[0]} | Crew: {zeile[1]} | Last: {zeile[2]} kg")

verbindung.close()