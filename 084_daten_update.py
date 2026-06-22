import sqlite3

print("\n=========================================")
print("--- LKW-UPDATE IM TRESOR AKTUALISIEREN ---")
print("=========================================")

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("UPDATE lkw_flotte SET last = 4500 WHERE id = 'HH-03'")
verbindung.commit()
verbindung.close()

print("🔄 Last für LKW HH-03 erfolgreich auf 4500 kg aktualisiert!")