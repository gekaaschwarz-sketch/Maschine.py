import sqlite3

print("\n=========================================")
print("--- 🌟 SQL SUPER-SUCHE v1.0 🌟 ---")
print("=========================================")

print("1: Nach LKW-ID suchen")
print("2: Nach Fahrer-Name suchen")

auswahl = input("Deine Auswahl: ")

if auswahl != "1" and auswahl != "2":
    print("⚠️ Ungültige Auswahl! Bitte starte das Skript neu und wähle 1 oder 2.")
    exit() # Dieser Befehl beendet das Python-Skript sofort!

verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

if auswahl == "1":
    such_id = input("Gib die LKW-ID ein: ")
    cursor.execute("SELECT * FROM lkw_flotte WHERE id = ?", (such_id,))
elif auswahl == "2":
    such_name = input("Gib den Namen ein: ")
    cursor.execute("SELECT * FROM lkw_flotte WHERE fahrer_in = ?", (such_name,))

ergebnis = cursor.fetchone()
if ergebnis:
    print(f"🎯 Gefunden! ID: {ergebnis[0]} | Fahrer*in: {ergebnis[1]} | Last: {ergebnis[2]} kg")
else:
    print("❌ Keine passenden Daten im Tresor gefunden!")

verbindung.close()