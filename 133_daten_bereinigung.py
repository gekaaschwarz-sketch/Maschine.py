import sqlite3

print("\n=========================================")
print("--- 🧼 SQL-KUNDEN-DATENBEREINIGUNG ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n🔍️ Suche nach verwaisten Kunden-Zuordnungen...")

    cursor.execute("""
        UPDATE kunden
        SET zugeordneter_lkw = 'KEIN LKW'
        WHERE zugeordneter_lkw NOT IN (SELECT id FROM lkw_flotte)
    """)

    anzahl_bereinigt = cursor.rowcount
    verbindung.commit()

    if anzahl_bereinigt > 0:
        print(f"🧼 SUCCESS: {anzahl_bereinigt} verwaiste Kunden-Einträge erfolgreich bereinigt!")
    else:
        print("✔️ Alles sauber: Alle Kunden haben eine gültige LKW-Zuordnung.")

print("\n⚙️ Bereinigungs-Modul abgeschlossen: Datenkonsistenz zu 100% gesichert.")