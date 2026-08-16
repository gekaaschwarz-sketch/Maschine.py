import sqlite3

print("\n=========================================")
print("---📊 PROFI-STATISTIK & LIMIT ---")
print("=========================================")

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("SELECT AVG(last) FROM lkw_flotte")
schnitt_ergebnis = cursor.fetchone()
durchschnitt = schnitt_ergebnis[0]
print(f"\n📈 Das Durchschnittsgewicht der Flotte beträgt: {durchschnitt} kg")

cursor.execute("SELECT * FROM lkw_flotte ORDER BY last DESC LIMIT 1")
spitzen_ergebnis = cursor.fetchone()
print(f"🥇 Der schwerste LKW aktuell: ID {spitzen_ergebnis[0]} ({spitzen_ergebnis[1]}) mit {spitzen_ergebnis[2]} kg.")

verbindung.close()