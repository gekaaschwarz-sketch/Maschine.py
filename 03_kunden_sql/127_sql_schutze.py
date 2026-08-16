import sqlite3

print("\n=========================================")
print("--- 🛡️ SQL-KRISEN-SCHUTZWALL v1.0 ---")
print("=========================================")

try:
    with sqlite3.connect("speditions_tresor.db") as verbindung:
        cursor = verbindung.cursor()

        cursor.execute("SELECT COUNT(*) FROM kunden")
        anzahl = cursor.fetchone()[0]

        print(f"\n📊 Datenbank-Zugriff erfolgreich!")
        print(f"👥 Aktuelle Kunden im Tresor: {anzahl}")

except sqlite3.Error as fehler:
    print("\n🚨 CRITICAL DATABASE ERROR AVERTED!")
    print(f"⚠️ Details vom SQL-System: {fehler}")
    print("🔄 Das Hauptprogramm bleibt krisensicher online!")

print("\n⚙️ Sicherheitsmodul aktiv: Festung Hamburg steht.")