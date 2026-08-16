import sqlite3

print("\n=========================================")
print("--- 🛡️ SQL-INJECTION-SCHUTZWALL v1.0 ---")
print("=========================================")

boese_hacker_eingabe = "Alster' OR '1'='1"

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n🕵️ Starte parametrisierten Sicherheits-Scan...")

    cursor.execute("SELECT * FROM kunden WHERE name = ?", (boese_hacker_eingabe,))
    ergebnisse = cursor.fetchall()

    print("\n🔎 Abfrage-Ergebnis:")
    if len(ergebnisse) == 0:
        print("🛡️ SUCCESS: Der Hacker-Angriff wurde eiskalt blockiert!")
        print("❌ Keine Daten manipuliert. Der Tresor bleibt absolut sicher.")
    else:
        print("🚨 ALARM: Sicherheits-Schutzwall durchbrochen! Daten gefährdet!")

print("\n⚙️ Sicherheits-Modul abgeschlossen: Festung Hamburg steht unzerstörbar.")