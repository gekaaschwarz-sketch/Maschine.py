import sqlite3

print("\n=========================================")
print("--- 🧹 KUNDEN-TRESOR KASSIEREN (RESET) ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()
    cursor.execute("DELETE FROM kunden")
    verbindung.commit()

print("\n✔️ Tabelle 'kunden' wurde komplett geleert! Der Tisch ist sauber.")