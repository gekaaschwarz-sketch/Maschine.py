import sqlite3

print("\n=========================================")
print("--- DYNAMISCHES LKW-UPDATE ---")
print("=========================================")

gesuchte_id = input("Welche LKW-ID möchtest du ändern? (z.B. HH-04): ")
neues_gewicht = int(input("Was ist das neue Gewicht in kg?: "))

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("UPDATE lkw_flotte SET last = ? WHERE id = ?", (neues_gewicht, gesuchte_id))

verbindung.commit()
verbindung.close()

print(f"🔄 LKW {gesuchte_id} wurde dynamisch auf {neues_gewicht} kg gesetzt!")