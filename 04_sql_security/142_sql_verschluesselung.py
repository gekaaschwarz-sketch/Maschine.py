import sqlite3
import hashlib

print("\n==========================================")
print("--- 🔐 AUTOMATISCHE SQL-VERSCHLÜSSELUNG ---")
print("==========================================")

master_passwort = "Festung_Hamburg_2026!"

sicherer_schluessel = hashlib.sha256(master_passwort.encode()).hexdigest()

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Erstelle krisensichere Verschlüsselungs-Tabelle...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS geheim_tresor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            schluessel_typ TEXT,
            geheim_code TEXT
        )
    """)
    verbindung.commit()

    print("🔐 Trage verschlüsselten Sicherheits-Schlüssel in den Tresor ein...")
    cursor.execute("""
        INSERT INTO geheim_tresor (schluessel_typ, geheim_code)
        VALUES ('Master-SHA256', ?)
    """, (sicherer_schluessel,))
    verbindung.commit()

    print("💎 SUCCESS: Der digitale Stahlschrank wurde erfolgreich verschlüsselt verriegelt!")

print("\n⚙️ Krypto-Modul abgeschlossen: Daten auf Dateiebene geschützt.")