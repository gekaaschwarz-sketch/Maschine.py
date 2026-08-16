import sqlite3

print("\n=========================================")
print("--- SQL-BLITZSUCHE NACH ID ---")
print("=========================================")

such_id = input("Welche LKW-ID suchst du genau?: ")

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("SELECT * FROM lkw_flotte WHERE id = ?", (such_id,))
ergebnis = cursor.fetchone()

if ergebnis:
    print(f"🎯 Treffer! Crew-Mitglied {ergebnis[1]} steuert diesen LKW mit {ergebnis[2]} kg Last.")
else:
    print("❌ Diese ID existiert nicht in unserem Stahlschrank!")

verbindung.close()