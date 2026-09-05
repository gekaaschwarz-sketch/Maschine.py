import sqlite3

print("\n=========================================")
print("--- 📊 COMBINED DISPO-REPORT (SQL JOIN) ---")
print("=========================================")

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("""
    SELECT kunden.name, kunden.zugeordneter_lkw, fleet_trucks.fahrer_in
    FROM kunden
    INNER JOIN fleet_trucks ON kunden.zugeordneter_lkw = fleet_trucks.id
""")
bericht_daten = cursor.fetchall()

print("\n📋️ LIVE-DATEN AUS DEM GEKOPPELTEN TRESOR:")
for zeile in bericht_daten:
    print(f"Firma: {zeile[0]} ➡️ LKW: {zeile[1]} ➡️ Crew: {zeile[2]}")

verbindung.close()