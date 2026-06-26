import sqlite3

print("\n=========================================")
print("--- 🧹 SQL-DATENBANK-BEREINIGUNG ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    cursor.execute("DELETE FROM kunden WHERE zugeordneter_lkw = 'HH-NULL'")
    verbindung.commit()

    cursor.execute("SELECT COUNT(*) FROM kunden")
    anzahl_kunden = cursor.fetchone()[0]

    print(f"\n🧹 Datenbank erfolgreich bereinigt!")
    print(f"👥 Bereinigter Zustand: Es sind noch {anzahl_kunden} echte Kunden im Tresor.")