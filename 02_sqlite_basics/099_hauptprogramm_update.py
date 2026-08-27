# Erweitert das SQL-Hauptmenue um das Aktualisieren der LKW-Last, abgesichert per try/except
import sqlite3

# Konfiguration: zentrale Konstanten für DB-Pfad und Tabellennamen
DB_PATH = "speditions_tresor.db"
DB_TABLE_LKW = "fleet_trucks"  # setze hier den tatsächlichen Tabellennamen


def lkw_existiert(db_path: str, truck_id: str) -> bool:
    """
    Prüft, ob ein LKW mit der gegebenen ID in der DB existiert.
    Gibt True zurück, wenn vorhanden, sonst False.
    """
    verbindung = sqlite3.connect(db_path)
    cursor = verbindung.cursor()
    try:
        cursor.execute(f"SELECT 1 FROM {DB_TABLE_LKW} WHERE id = ? LIMIT 1", (truck_id,))
        return cursor.fetchone() is not None
    finally:
        verbindung.close()


def delete_lkw(db_path: str, truck_id: str) -> bool:
    """
    Löscht einen LKW mit der gegebenen ID.
    Gibt True zurück, wenn eine Zeile gelöscht wurde, sonst False.
    Commit nur bei Löschung; rollback bei 0 Zeilen.
    """
    verbindung = sqlite3.connect(db_path)
    cursor = verbindung.cursor()
    try:
        cursor.execute(f"DELETE FROM {DB_TABLE_LKW} WHERE id = ?", (truck_id,))
        if cursor.rowcount > 0:
            verbindung.commit()
            return True
        else:
            verbindung.rollback()
            return False
    finally:
        verbindung.close()


def update_lkw_last(db_path: str, truck_id: str, neue_last: int) -> bool:
    """
    Aktualisiert die Spalte 'last' für den LKW mit der gegebenen ID.
    Returns True if a row was updated, False if no row matched.

    Commit wird nur bei tatsächlicher Änderung ausgeführt; ansonsten rollback.
    """
    verbindung = sqlite3.connect(db_path)
    cursor = verbindung.cursor()
    try:
        cursor.execute(f"UPDATE {DB_TABLE_LKW} SET last = ? WHERE id = ?", (neue_last, truck_id))
        if cursor.rowcount > 0:
            verbindung.commit()
            return True
        else:
            verbindung.rollback()
            return False
    finally:
        verbindung.close()


def main() -> int:
    while True:
        print("\n=====================================")
        print("--- 🚛 SPEDITION HAMBURG SQL ---")
        print("=====================================")
        print("1: Flotte anzeigen")
        print("2: LKW hinzufügen")
        print("3: LKW löschen")
        print("5: LKW-Last aktualisieren")
        print("4: Beenden")

        auswahl = input("\nDeine Auswahl: ")

        if auswahl == "1":
            verbindung = sqlite3.connect(DB_PATH)
            cursor = verbindung.cursor()
            cursor.execute(f"SELECT * FROM {DB_TABLE_LKW}")
            alle_lkw = cursor.fetchall()

            print("\n--- 🗄️ SQL-TRESOR: AKTUELLE FLOTTE ---")
            for zeile in alle_lkw:
                print(f"ID: {zeile[0]} | Fahrer_in: {zeile[1]} | Last: {zeile[2]} kg")

            verbindung.close()

        elif auswahl == "2":
            print("\n--- 📥️ NEUEN LKW REGISTRIEREN ---")
            neue_id = input("Gib die neue LKW-ID ein: ")
            neuer_fahrer = input("Wer ist der Fahrer / die Fahrerin?: ")
            try:
                neue_last = int(input("Wie viele kg Last hat der LKW?: "))
            except ValueError:
                print("\n⚠️ FEHLER: Du musst eine echte Zahl eingeben! Vorgang abgebrochen.")
                continue

            verbindung = sqlite3.connect(DB_PATH)
            cursor = verbindung.cursor()

            cursor.execute(f"INSERT INTO {DB_TABLE_LKW} (id, fahrer_in, last) VALUES (?, ?, ?)",
                           (neue_id, neuer_fahrer, neue_last))
            verbindung.commit()
            verbindung.close()

            print(f"✔️ LKW {neue_id} erfolgreich im SQL-Tresor verankert!")

        elif auswahl == "3":
            print("\n--- 🗑️ LKW-ID AUS TRESOR LÖSCHEN ---")
            print("(Tippe 'X' ein, um den Vorgang abzubrechen)")
            loesch_id = input("Welche LKW-ID soll gelöscht werden? (z.B. HH-06): ")

            if loesch_id.lower() == "x":
                print("\n❌ Löschvorgang abgebrochen. Zurück zum Hauptmenü!")
                continue

            deleted = delete_lkw(DB_PATH, loesch_id)
            if deleted:
                print(f"\n🗑️ LKW {loesch_id} wurde erfolgreich aus dem SQL-Tresor entfernt!")
            else:
                print(f"\n⚠️ Kein LKW mit ID '{loesch_id}' gefunden — nichts gelöscht.")

        elif auswahl == "5":
            print("\n--- 🔄 LKW-LAST IM TRESOR AKTUALISIEREN ---")
            print("(Tippe 'X' ein, um den Vorgang abzubrechen)")
            update_id = input("Welche LKW-ID möchtest du ändern? (z.B. HH-04): ")

            if update_id.lower() == "x":
                print("\n❌ Vorgang abgebrochen. Zurück zum Hauptmenü!")
                continue

            # Prüfe Existenz VOR der Abfrage der neuen Last
            if not lkw_existiert(DB_PATH, update_id):
                print(f"\n⚠️ Kein LKW mit ID '{update_id}' gefunden — kein Update durchgeführt.")
                continue

            try:
                neue_last = int(input("Was ist das neue Gewicht in kg?: "))
            except ValueError:
                print("\n⚠️ FEHLER: Du musst eine echte Zahl eingeben! Vorgang abgebrochen.")
                continue

            # Verwende die helper-Funktion und prüfe das Ergebnis
            updated = update_lkw_last(DB_PATH, update_id, neue_last)
            if updated:
                print(f"\n🔄 LKW {update_id} wurde dynamisch auf {neue_last} kg gesetzt!")
            else:
                # Dieses Zweig sollte bei vorheriger Existenzprüfung selten treten,
                # kann aber bei Race‑Conditions auftauchen.
                print(f"\n⚠️ Update für LKW '{update_id}' konnte nicht durchgeführt werden.")

        elif auswahl == "4":
            print("\nTschüss, Valentin! Sichere Fahrt!")
            break

        else:
            print("Ungültige Auswahl. Bitte erneut versuchen.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())