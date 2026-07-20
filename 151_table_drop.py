import sqlite3

print("\n=========================================")
print("--- 🗑️ AUTOMATISCHES SQL-TABELLEN-DROP ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Starte dsgvo-konforme Tabellen-Vernichtung...")

    cursor.execute("DROP TABLE IF EXISTS kunden_sandbox;")

    verbindung.commit()
    print("💎 SUCCESS: Tabelle 'kunden_sandbox' restlos von der SSD gefegt!")

print("\n⚙️ Drop-Modul abgeschlossen: Datenrückstände erfolgreich vernichtet.")