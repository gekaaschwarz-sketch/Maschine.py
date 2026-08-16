import sqlite3

print("\n=========================================")
print("--- SQL-TABELLENSTRUKTUR ERSTELLEN ---")
print("=========================================")

# 1. Verbindung zum bestehenden Tresor herstellen
verbindung = sqlite3.connect("speditions_tresor.db")
cursor = verbindung.cursor()

# 2. Der SQL-Befehl zum Erstellen des Stahlschranks (Tabelle)
# "IF NOT EXISTS" sorgt dafür, dass das Programm nicht abstürzt, wenn die Tabelle schon da ist!
cursor.execute("""
CREATE TABLE IF NOT EXISTS lkw_flotte (
    id TEXT,
    fahrer_in TEXT,
    last INTEGER
)
""")

print("⚙️ Wächter: Die Struktur für 'lkw_flotte' wurde erfolgreich zementiert!")

# 3. Die Änderungen permanent auf der 1-TB-SSD speichern und schließen
verbindung.commit()
verbindung.close()
print("🔒️ Änderungen gespeichert. Tresor wieder sicher verschlossen.")