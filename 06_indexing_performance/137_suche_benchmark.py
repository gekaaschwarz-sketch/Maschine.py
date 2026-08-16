import sqlite3
import time

print("\n=========================================")
print("--- ⏱️ SQL-PERFORMANCE-BENCHMARK ---")
print("=========================================")

suchbegriff = "Alster"
such_muster = f"%{suchbegriff}%"

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print(f"\n⚡️ Starte Hochgeschwindigkeits-Suche für '{suchbegriff}'...")

    start_zeit = time.perf_counter()

    cursor.execute("SELECT * FROM kunden WHERE name LIKE ?", (such_muster,))
    ergebnisse = cursor.fetchall()

    end_zeit = time.perf_counter()

    laufzeit_ms = (end_zeit - start_zeit) * 1000

    print("\n🔎 Ergebnisse aus dem Stahlschrank geholt:")
    for kunde in ergebnisse:
        print(f"🏢 Firma: {kunde[1]} | LKW: {kunde[2]}")

    print("\n=========================================")
    print(f"⏱️ BENCHMARK: Abfrage dauerte exakt {laufzeit_ms:.4f} Millisekunden!")
    print("=========================================")

print("\n⚙️ Performance-Modul abgeschlossen: Triebwerke optimal kalibriert.")