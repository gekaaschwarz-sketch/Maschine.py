import sqlite3

print("\n=========================================")
print("--- 🛡️ SQL-TRANSAKTION-WALL (ROLLBACK) ---")
print("=========================================")

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

try:
    print("\n⚡️ Starte kritische Doppel-Buchung...")

    cursor.execute("INSERT INTO kunden (name, zugeordneter_lkw) VALUES ('Zoll-Abfertigung Nord', 'HH-99')")

    cursor.execute("UPDATE lkw_flotte SET gewitter = 'FEHLER' WHERE id = 1")

    verbindung.commit()
    print("✔️ Erfolg: Beide Buchungen fehlerfrei eingebrannt!")

except sqlite3.Error as fehler:
    print("\n🚨 CRITICAL ERROR DURING TRANSACTION DETECTED!")
    print(f"⚠️ SQL-Fehlermeldung: {fehler}")
    print("🔄 Zünde ROLLBACK: Unvollständige Daten werden restlos gelöscht!")

    verbindung.rollback()
    print("🛡️ Stahlschrank gerettet: Der Tisch ist wieder absolut sauber.")

finally:
    verbindung.close()

print("\n⚙️ Transaktion-Modul abgeschlossen: Keine halben Daten im System.")