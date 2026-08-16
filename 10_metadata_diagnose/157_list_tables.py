import sqlite3

print("\n==========================================")
print("--- 📂 AUTOMATISCHE TABELLEN-AUFLISTUNG ---")
print("==========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n🕵️ Durchleuchte System-Metadaten (sqlite_master)...")
    try:
        cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name NOT LIKE 'sqlite_%';
        """)
        tabellen_liste = cursor.fetchall()

        print("\n📋️ Im Speditions-Tresor existieren folgende Tabellen:")
        print("-" * 50)

        for index, tabelle in enumerate(tabellen_liste, start=1):
            print(f"📦️ Tabelle {index}: {tabelle[0]}")

    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER BEIM METADATEN-SCAN: {fehler}")

print("\n⚙️ System-Scan abgeschlossen: Alle Tabellen erfolgreich identifiziert.")