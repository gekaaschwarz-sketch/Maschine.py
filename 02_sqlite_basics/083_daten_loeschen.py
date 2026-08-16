import sqlite3

print("\n=========================================")
print("--- LKW AUS TRESOR LÖSCHEN ---")
print("=========================================")

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("DELETE FROM lkw_flotte WHERE id = 'HH-02'")

verbindung.commit()
verbindung.close()

print("🗑️ LKW HH-02 erfolgreich aus dem SQL-Tresor gelöscht!")