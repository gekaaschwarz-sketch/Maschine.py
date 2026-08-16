import sqlite3

print("\n" + "=" * 55)
print("--- 🔍 AUTOMATISIERTER DATENBANK-GESUNDHEITSCHECK ---")
print("=" * 55)

datenbank = "speditions_tresor.db"

print(f"\nPrüfe Integrität von '{datenbank}'...")

try:
    with sqlite3.connect(datenbank) as verbindung:
        cursor = verbindung.cursor()

        cursor.execute("PRAGMA integrity_check;")
        ergebnis = cursor.fetchall()

        if len(ergebnis) == 1 and ergebnis[0][0] == "ok":
            print("✅ Datenbank ist strukturell intakt.")
        else:
            print("🚨 PROBLEME GEFUNDEN:")
            for zeile in ergebnis:
                print(f"   - {zeile[0]}")

        cursor.execute("PRAGMA foreign_key_check;")
        fk_probleme = cursor.fetchall()

        if not fk_probleme:
            print("✅ Keine Fremdschlüssel-Verletzungen gefunden.")
        else:
            print(f"⚠️ {len(fk_probleme)} Fremdschlüssel-Verletzung(en) gefunden.")

except sqlite3.Error as fehler:
    print(f"🚨 FEHLER BEIM CHECK: {fehler}")

print("\n" + "=" * 45)
print("Gesundheitscheck abgeschlossen.")
print("=" * 45)