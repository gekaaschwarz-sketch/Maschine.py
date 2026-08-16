import sqlite3

print("\n=============================================")
print("--- SQLITE-DATENBANK-TRESOR STARTEN ---")
print("=============================================")

# 1. Verbindung zum Tresor herstellen (Die Datei wird automatisch angelegt!)
verbindung = sqlite3.connect("speditions_tresor.db")

# 2. Den Cursor erstellen (Das ist unser Arbeiter für die SQL-Befehle)
cursor = verbindung.cursor()

print("✅ Erfolg: Die Datenbank 'speditions_tresor.db' wurde unzerstörbar erstellt!")

# 3. Den Tresor wieder sicher verschließen
verbindung.close()
print("🔒️ Verbindung sicher beendet.")