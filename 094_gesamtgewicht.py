import sqlite3

print("\n=========================================")
print("--- 📊 FLOTTEN-STATISTIK: GESAMTGEWICHT ---")
print("=========================================")

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("SELECT SUM(last) FROM lkw_flotte")
ergebnis = cursor.fetchone()

gesamt_last = ergebnis[0]
print(f"\n⚖️ Gesamtgewicht aller LKWs im Hafen: {gesamt_last} kg")

verbindung.close()