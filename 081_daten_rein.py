import sqlite3

print("\n=========================================")
print("--- LKW-DATEN IN TRESOR LADEN ---")
print("=========================================")

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("INSERT INTO lkw_flotte (id, fahrer_in, last) VALUES ('HH-99', 'Maren', 5000)")
cursor.execute("INSERT INTO lkw_flotte (id, fahrer_in, last) VALUES ('HH-02', 'Yvonne', 4)")
cursor.execute("INSERT INTO lkw_flotte (id, fahrer_in, last) VALUES ('HH-03', 'Stefan', 3800)")
cursor.execute("INSERT INTO lkw_flotte (id, fahrer_in, last) VALUES ('HH-04', 'Hannes', 2000)")

verbindung.commit()
verbindung.close()

print("🔒️ Daten sicher im SQL-Tresor eingebrannt!")