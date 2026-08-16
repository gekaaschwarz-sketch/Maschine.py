import sqlite3
import time

print("\n" + "=" * 47)
print("--- 🔒 TRANSAKTIONS-SPERRE MIT TIMEOUT-TEST ---")
print("=" * 47)

verbindung1 = sqlite3.connect("speditions_tresor.db")
cursor1 = verbindung1.cursor()

verbindung2 = sqlite3.connect("speditions_tresor.db")
verbindung2.execute("PRAGMA busy_timeout = 5000;")  # Geduld: 5 Sekunden warten
cursor2 = verbindung2.cursor()

try:
    print("\n⚡ Verbindung 1: Sperre die Tabelle exklusiv...")
    cursor1.execute("BEGIN EXCLUSIVE;")
    cursor1.execute("UPDATE fleet_trucks SET payload_tons = 15 WHERE id = 1;")
    print("🔒 Verbindung 1 hält die exklusive Sperre.")

    print("\n⏳ Verbindung 2 versucht jetzt gleichzeitig zu schreiben...")
    start = time.time()
    try:
        cursor2.execute("UPDATE fleet_trucks SET payload_tons = 20 WHERE id = 2;")
        print("✅ Verbindung 2 konnte trotz Sperre schreiben (Sperre war schon frei).")
    except sqlite3.OperationalError as fehler:
        dauer = round(time.time() - start, 2)
        print(f"⏱️ Verbindung 2 wartete {dauer} Sekunden und brach dann ab: {fehler}")

    verbindung1.commit()
    print("\n🔓 Verbindung 1 gibt die Sperre wieder frei.")

except sqlite3.Error as fehler:
    print(f"🚨 FEHLER IM TEST: {fehler}")
finally:
    verbindung1.close()
    verbindung2.close()

print("\n" + "=" * 50)
print("⚙️ Test abgeschlossen: Timeout-Verhalten überprüft.")
print("=" * 50)