# Hauptprogramm fuer Flottenverwaltung: Anzeigen, Hinzufuegen, Loeschen, Last aktualisieren, Beenden

from flotten_modul_191 import FlottenVerwaltung

DB_PATH = "speditions_tresor.db"


def main(db_pfad: str = DB_PATH) -> int:
    """
    Einfaches Textmenue, das die FlottenVerwaltung nutzt.

    :param db_pfad: Pfad zur SQLite-DB (ermoeglicht Tests auf einer DB-Kopie)
    :return: exit code
    """
    verw = FlottenVerwaltung(db_pfad)

    while True:
        print("\n=========================================")
        print("--- SPEDITION: HAUPTMENUE FLOTTE -------")
        print("=========================================")
        print("1: Flotte anzeigen")
        print("2: LKW hinzufuegen")
        print("3: LKW loeschen")
        print("5: LKW-Last aktualisieren")
        print("4: Beenden")

        auswahl = input("\nDeine Auswahl: ").strip()

        if auswahl == "1":
            # Anzeige aller LKWs
            alle = verw.alle()
            print("\n--- AKTUELLE FLOTTE ---")
            if not alle:
                print("Keine Eintraege vorhanden.")
            else:
                for l in alle:
                    # explizite Spalten-Ausgabe
                    print(f"ID: {l.id} | Fahrer_in: {l.fahrer_in} | Last: {l.last} kg")

        elif auswahl == "2":
            # Hinzufuegen mit Zahlpruefung fuer last
            print("\n--- LKW HINZUFUEGEN ---")
            neue_id = input("Gib die neue LKW-ID ein: ").strip()
            neuer_fahrer = input("Gib den Namen der Fahrer_in ein: ").strip()
            last_str = input("Wie viele kg Last hat der LKW? ").strip()
            try:
                neue_last = int(last_str)
            except ValueError:
                print("Ungueltige Zahl fuer Last. Vorgang abgebrochen.")
                continue

            try:
                ok = verw.hinzufuegen(neue_id, neuer_fahrer, neue_last)
                if ok:
                    print(f"LKW {neue_id} erfolgreich hinzugefuegt.")
                else:
                    # Die Methode gibt True bei Erfolg, sonst wuerde sie bis hier nicht ohne Exception gelangen
                    print(f"LKW {neue_id} wurde nicht hinzugefuegt.")
            except ValueError as ve:
                # Duplikat vom Modul gemeldet
                print(f"Fehler: {ve}")

        elif auswahl == "3":
            # Loeschen mit Abbruchoption 'x'
            print("\n--- LKW LOESCHEN ---")
            loesch_id = input("Welche LKW-ID soll geloescht werden? (Tippe 'x' zum Abbrechen): ").strip()
            if loesch_id.lower() == "x":
                print("Loeschvorgang abgebrochen.")
                continue
            try:
                deleted = verw.loeschen(loesch_id)
                if deleted:
                    print(f"LKW {loesch_id} erfolgreich geloescht.")
                else:
                    print(f"Kein LKW mit ID '{loesch_id}' gefunden. Nichts geloescht.")
            except Exception as e:
                print(f"Fehler beim Loeschen: {e}")

        elif auswahl == "5":
            # Last aktualisieren; Existenz pruefen bevor neue Last eingegeben wird
            print("\n--- LKW-LAST AKTUALISIEREN ---")
            up_id = input("Welche LKW-ID moechtest du aendern? (Tippe 'x' zum Abbrechen): ").strip()
            if up_id.lower() == "x":
                print("Vorgang abgebrochen.")
                continue

            # Existenzpruefung via suchen()
            vorhand = verw.suchen(up_id)
            if vorhand is None:
                print(f"Kein LKW mit ID '{up_id}' gefunden. Kein Update durchgefuehrt.")
                continue

            last_str = input("Gib die neue Last in kg ein: ").strip()
            try:
                neue_last = int(last_str)
            except ValueError:
                print("Ungueltige Zahl fuer Last. Vorgang abgebrochen.")
                continue

            try:
                updated = verw.last_aktualisieren(up_id, neue_last)
                if updated:
                    print(f"LKW {up_id} erfolgreich auf {neue_last} kg gesetzt.")
                else:
                    print(f"Update konnte nicht durchgefuehrt werden (keine Zeile betroffen).")
            except Exception as e:
                print(f"Fehler beim Update: {e}")

        elif auswahl == "4":
            print("\nAuf Wiedersehen!")
            return 0

        else:
            print("Ungueltige Auswahl. Bitte erneut versuchen.")


if __name__ == "__main__":
    raise SystemExit(main())