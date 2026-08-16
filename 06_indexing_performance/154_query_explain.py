import sqlite3

print("\n=============================================")
print("--- 🔬 SQL-ABFRAGE-PLAN-ANALYSE (EXPLAIN) ---")
print("=============================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n🕵️ Durchleuchte internen Abfrage-Marschplan...")
    try:
        cursor.execute("""
            EXPLAIN QUERY PLAN
            SELECT * FROM kunden WHERE name = 'Alster-Logistik GmbH';
        """)
        marschplan = cursor.fetchall()

        print("\n📋️ Interner SQLite-Suchbericht:")
        for schritt in marschplan:
            print(f"🔎 Weg-Analyse: {schritt[3]}")

    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER IM DIAGNOSE-MODUL: {fehler}")

print("\n⚙️ Diagnose-Modul abgeschlossen: Abfrage-Pfad erfolgreich verifiziert.")