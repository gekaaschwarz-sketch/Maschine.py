import sqlite3

print("\n=========================================")
print("--- ⚙️ AUTOMATISCHES SQL-INDEX-TUNING ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Optimiere Datenbank-Struktur...")

    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_kunden_lkw
        ON kunden (zugeordneter_lkw)
    """)

    verbindung.commit()
    print("💎 SUCCESS: Highspeed-Index 'idx_kunden_lkw' erfolgreich im Stahlschrank verankert!")

print("\n⚙️ Tuning-Modul abgeschlossen: Abfrage-Triebwerke voll optimiert.")