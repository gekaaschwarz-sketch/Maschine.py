import sqlite3

print("\n=========================================")
print("--- 🧼 AUTOMATISCHE TABELLEN-LEERUNG ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Starte radikale Tabellen-Entleerung (TRUNCATE)...")

    cursor.execute("DELETE FROM kunden_sandbox;")

    cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'kunden_sandbox';")

    verbindung.commit()
    print("💎 SUCCESS: Tabelle 'kunden_sandbox' komplett geleert und ID-Zähler auf 0 gesetzt!")

print("\n⚙️ Truncate-Modul abgeschlossen: Testumgebung perfekt gesäubert.")