import sqlite3

print("\n=========================================")
print("--- 🗺️ MULTI-SUCHE: KUNDE & FLOTTE ---")
print("=========================================")

suchbegriff = "Thomas"
such_muster = f"%{suchbegriff}%"

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    cursor.execute("""
        SELECT kunden.name, kunden.zugeordneter_lkw, fleet_trucks.fahrer_in
        FROM kunden
        LEFT JOIN fleet_trucks ON kunden.zugeordneter_lkw = fleet_trucks.id
        WHERE kunden.name LIKE ? OR fleet_trucks.fahrer_in LIKE ?
    """, (such_muster, such_muster))

    ergebnisse = cursor.fetchall()

    print(f"\n🔎 Globale Suchergebnisse für '{suchbegriff}':")

    if len(ergebnisse) == 0:
        print("❌ Keine passende Einträge in gesamten System gefunden.")
    else:
        for zeile in ergebnisse:
            print(f"🏢 Kunde: {zeile[0]} | 🚛 LKW: {zeile[1]} | 👥 Crew: {zeile[2]}")
print("\n⚙️ Multi-Suche abgeschlossen: Maximale Freiheit für die Disposition.")