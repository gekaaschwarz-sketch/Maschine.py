import sqlite3
import datetime

print("\n=========================================")
print("--- 🚨 AUTOMATISCHER SQL-ERROR-LOGGER ---")
print("=========================================")

try:
    with sqlite3.connect("speditions_tresor.db") as verbindung:
        cursor = verbindung.cursor()

        print("\n⚡️ Provoziere absichtlich einen System-Fehler...")

        cursor.execute("SELECT * FROM geister_tabelle")
        daten = cursor.fetchall()

except sqlite3.Error as fehler:
    zeitstempel = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_nachricht = f"🕒️ [{zeitstempel}] | 🚨 SQL-FEHLER: {fehler}\n"

    print(f"\n💥 SYSTEM-ABSTURZ ABGEFANGEN! Schreibe Details in den Sicherheits-Ordner...")

    with open("error.log", mode="a", encoding="utf-8") as log_datei:
        log_datei.write(log_nachricht)

    print("📝 SUCCESS: Der Fehler wurde unlöschbar im 'error.log' protokolliert!")

print("\n⚙️ Error-Logger abgeschlossen: System-Stabilität zu 100% garantiert.")