import sqlite3

print("\n==========================================")
print("--- ⚙️ AUTOMATISCHE SPALTEN-UMBENENNUNG ---")
print("==========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n⚡️ Starte Struktur-Modernisierung der LKW-Flotte...")
    try:
        cursor.execute("ALTER TABLE lkw_flotte RENAME COLUMN nutzlast_tonnen TO payload_tons;")
        verbindung.commit()
        print("💎 SUCCESS: Spalte erfolgreich in 'payload_tons' umbenannt!")

        print("\n📋️ Überprüfe modernisierte Struktur der LKW-Tabelle:")
        cursor.execute("PRAGMA table_info(lkw_flotte);")
        neue_dna = cursor.fetchall()

        for spalte in neue_dna:
            print(f"📦️ Spalte: {spalte[1]} | Typ: {spalte[2]} | Standartwerd: {spalte[4]}")

    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER BEIM SPALTEN-RENAME: {fehler}")

print("\n⚙️ Umbenennungs-Modul abgeschlossen: Spalten-Architektur erfolgreich internationalisiert.")