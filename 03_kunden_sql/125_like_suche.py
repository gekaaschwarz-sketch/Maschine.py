import sqlite3

print("\n=========================================")
print("--- 🔍️ SQL-SMART-SUCHE (WILD-CARDS) ---")
print("=========================================")

suchbegriff = "Alster"

such_muster = f"%{suchbegriff}%"

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    cursor.execute("SELECT * FROM kunden WHERE name LIKE ?", (such_muster,))
    such_ergebnisse = cursor.fetchall()

    print(f"\n🔎 Suchergebnis für den Begriff '{suchbegriff}':")

    if len(such_ergebnisse) == 0:
        print("❌ Keine passenden Kunden im Tresor gefunden.")
    else:
        for kunde in such_ergebnisse:
            print(f"🏢 Firma: {kunde[1]} | Zugeordneter LKW-Index: {kunde[2]}")

print("\n⚙️ Such-Modul abgeschlossen: Volle Flexibilität für den Disponenten.")