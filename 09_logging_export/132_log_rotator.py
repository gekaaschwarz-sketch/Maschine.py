import sqlite3

print("\n=========================================")
print("--- 🧹 AUTOMATISCHER SQL-LOG-ROTATOR ---")
print("=========================================")

max_logs = 5

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    cursor.execute("SELECT COUNT(*) FROM system_log")
    aktuelle_anzahl = cursor.fetchone()[0]
    print(f"📊 Aktuelle Log-Einträge im System: {aktuelle_anzahl}")

    if aktuelle_anzahl > max_logs:
        ueberschuss = aktuelle_anzahl - max_logs
        print(f"⚠️ Limit von {max_logs} überschritten! Lösche {ueberschuss} alte Einträge...")

        cursor.execute("""
            DELETE FROM system_log
            WHERE id IN (SELECT id FROM system_log ORDER BY zeitstempel ASC LIMIT ?)
        """, (ueberschuss,))

        verbindung.commit()
        print("🧹 SUCCESS: Alte Log-Einträge erfolgreich rotiert und gelöscht!")
    else:
        print("✔️ Alles im grünen Bereich: Kein Speicherplatz-Risiko vorhanden.")

print("\n⚙️ Rotator-Modul abgeschlossen: Speicherplatz der Datenbank optimiert.")