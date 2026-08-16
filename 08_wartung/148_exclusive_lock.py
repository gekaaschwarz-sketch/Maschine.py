import sqlite3
import time

print("\n============================================")
print("--- 🔒️ EXKLUSIVE SQL-TRANSAKTIONS-SPERRE ---")
print("============================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n🔒️ Aktiviere exklusiven Stahlschrank-Schutz (LOCK)...")
    try:
        cursor.execute("BEGIN EXCLUSIVE TRANSACTION;")

        print("⚡️ Führe kritische LKW-Zuweisung im Hafen durch...")
        cursor.execute("""
            UPDATE kunden
            SET zugeordneter_lkw = 'HH-99'
            WHERE name = 'Alster-Logistik GmbH';
        """)

        time.sleep(2)

        verbindung.commit()
        print("💎 SUCCESS: Buchung krisensicher eingebrannt. Tresor wieder geöffnet!")
    except sqlite3.Error as fehler:
        verbindung.rollback()
        print(f"🚨 TRANSAKTIONS-ABSTURZ: {fehler}")

print("\n⚙️ Sperr-Modul abgeschlossen: Daten-Konsistenz absolut garantiert.")