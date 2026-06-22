import sqlite3

print("\n=========================================")
print("---📊 FLOTTEN-STATISTIK: ANZAHL ---")
print("=========================================")

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

cursor.execute("SELECT COUNT(*) FROM lkw_flotte")

ergebnis = cursor.fetchone()

anzahl_lkw = ergebnis[0] # ❌ HIER KNALLT ES!
print(f"\n📈 Aktueller Status: Es sind insgesamt {anzahl_lkw} LKWs im Tresor registriert.")

verbindung.close()