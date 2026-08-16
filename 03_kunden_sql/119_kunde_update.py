import sqlite3

print("\n=========================================")
print("--- 👥 SQL-KUNDEN-DISPO-UPDATE ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    neuer_lkw = "HH-05"
    kunde_name = "Hamburg-Kaffee AG"

    cursor.execute("UPDATE kunden SET zugeordneter_lkw = ? WHERE name = ?", (neuer_lkw, kunde_name))
    verbindung.commit()

    print(f"\n🔄 Dispo-Update erfolgreich!")
    print(f"🚛 {kunde_name} wird ab jetzt von LKW {neuer_lkw} bedient.")