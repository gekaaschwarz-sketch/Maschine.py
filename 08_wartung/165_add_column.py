import sqlite3

print("\n=========================================")
print("--- ⚙️ AUTOMATISCHE SPALTEN-ERWEITERUNG ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Starte dynamische Tabellen-Erweiterung der LKW-Flotte...")
    try:
        cursor.execute("ALTER TABLE lkw_flotte ADD COLUMN nutzlast_tonnen INTEGER DEFAULT 12;")
        verbindung.commit()
        print("💎 SUCCESS: Neue Spalte 'nutzlast_tonnen' erfolgreich im laufenden Betrieb implantiert!")

        print("\n📋️ Überprüfe modifizierte Struktur der LKW-Tabelle:")
        cursor.execute("PRAGMA table_info(lkw_flotte);")
        neue_dna = cursor.fetchall()

        for spalte in neue_dna:
            print(f"📦️ Spalte: {spalte[1]} | Typ: {spalte[2]} | Standardwert: {spalte[4]}")

    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER BEIM TABELLEN-UPGRADE: {fehler}")

print("\n⚙️ Upgrade-Modul abgeschlossen: Datenbank-Struktur erfolgreich modernisiert.")