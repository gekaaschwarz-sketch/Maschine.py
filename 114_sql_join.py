import sqlite3

print("\n=========================================")
print("--- 📊 COMBINED DISPO-REPORT (SQL JOIN) ---")
print("=========================================")

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("""
    SELECT kunden.name, kunden.zugeordneter_lkw, lkw_flotte.fahrer_in
    FROM kunden
    INNER JOIN lkw_flotte ON kunden.zugeordneter_lkw = lkw_flotte.id
""")
bericht_daten = cursor.fetchall()

print("\n📋️ LIVE-DATEN AUS DEM GEKOPPELTEN TRESOR:")
for zeile in bericht_daten:
    print(f"Firma: {zeile[0]} ➡️ LKW: {zeile[1]} ➡️ Crew: {zeile[2]}")

verbindung.close()