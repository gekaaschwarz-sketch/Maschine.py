import sqlite3

print("\n=========================================")
print("--- 🌿 FEATURE-BRANCH: SUPER-STATISTIK ---")
print("=========================================")

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("SELECT COUNT(*) FROM lkw_flotte")
anzahl = cursor.fetchone()[0]

cursor.execute("SELECT SUM(last) FROM lkw_flotte")
gesamt_gewicht = cursor.fetchone()[0]

print(f"📈 Aktive LKW in Hafen: {anzahl} Fahrzeuge")
print(f"⚖️ Geladenes Gesamtgewicht: {gesamt_gewicht} kg")

verbindung.close()