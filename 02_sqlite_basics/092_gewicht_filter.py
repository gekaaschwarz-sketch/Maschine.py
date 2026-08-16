import sqlite3

print("\n=========================================")
print("--- HOCHLAST-FILTER (> 4000 kg) ---")
print("=========================================")

grenze = int(input("Zeige LKWs mit mehr Last als (in kg): "))

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("SELECT * FROM lkw_flotte WHERE last > ?", (grenze,))
gefilterte_lkw = cursor.fetchall()

print(f"\n--- 🚛 LKWs ÜBER {grenze} kg ---")
for zeile in gefilterte_lkw:
    print(f"LKW: {zeile[0]} | Crew: {zeile[1]} | Last: {zeile[2]} kg")

verbindung.close()