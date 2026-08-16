import sqlite3

print("\n=========================================")
print("--- 👥 SQL-KUNDEN-ZENTRALE v1.0 ---")
print("=========================================")

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS kunden (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT, 
    zugeordneter_lkw TEXT
)
""")

cursor.execute("INSERT INTO kunden (name, zugeordneter_lkw) VALUES ('Hamburg-Kaffee AG', 'HH-99')")
cursor.execute("INSERT INTO kunden (name, zugeordneter_lkw) VALUES ('Alster-Logistik GmbH', 'HH-05')")

verbindung.commit()
verbindung.close()

print("\n✔️ Kunden-Tabelle erfolgreich erstellt und Test-Kunden registriert!")