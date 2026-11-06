import os
import sqlite3
import sys
from pathlib import Path

print("\n=========================================")
print("--- 🛡️ AUTOMATISCHE BACKUP-TÜV-CHECK ---")
print("=========================================")

# Aufruf: python3 136_backup_check.py [Pfad] [--pflicht tabelle1,tabelle2]

backup_datei = "speditions_tresor_BACKUP.db"
live_datei = "speditions_tresor.db"

# Pflichttabellen: fehlt eine davon, ist die Sicherung unbrauchbar (Exitcode 3).
PFLICHT_TABELLEN = ("fleet_trucks", "kunden", "system_log")
# Optionale/historische Tabellen: fehlt eine, gibt es nur einen Hinweis.
OPTIONALE_TABELLEN = (
    "fleet_trucks_backup_snapshot",
    "kunden_wiederhergestellt",
    "fuhrpark_fleet",
)

# Exitcodes (fuer Skripte und Tests):
#   0 = Struktur intakt, alle Pflichttabellen vorhanden
#   1 = Sicherungsdatei fehlt
#   2 = keine gueltige SQLite-Datei oder integrity_check meldet Fehler
#   3 = Datei intakt, aber mindestens eine Pflichttabelle fehlt
#   4 = falscher Aufruf (unbekannte Option, fehlender Wert)
# Hinweise (0 Zeilen, optionale Tabellen, Live-Vergleich) aendern den Exitcode nicht.
EXIT_OK = 0
EXIT_DATEI_FEHLT = 1
EXIT_UNGUELTIG = 2
EXIT_PFLICHT_FEHLT = 3
EXIT_AUFRUF = 4


class AufrufFehler(Exception):
    pass


def argumente_lesen(argumente):
    """Liefert (pfad, pflicht_tabellen). Wirft AufrufFehler bei falscher Benutzung."""
    pfad = None
    pflicht = PFLICHT_TABELLEN
    i = 0
    while i < len(argumente):
        arg = argumente[i]
        if arg == "--pflicht" or arg.startswith("--pflicht="):
            if arg == "--pflicht":
                i += 1
                if i >= len(argumente):
                    raise AufrufFehler("--pflicht braucht eine Liste, z. B. --pflicht fleet_trucks,kunden")
                wert = argumente[i]
            else:
                wert = arg.split("=", 1)[1]
            namen = tuple(n.strip() for n in wert.split(",") if n.strip())
            if not namen:
                raise AufrufFehler("--pflicht enthaelt keinen Tabellennamen")
            pflicht = namen
        elif arg.startswith("--"):
            raise AufrufFehler(f"Unbekannte Option: {arg}")
        else:
            if pfad is not None:
                raise AufrufFehler("Es darf nur ein Pfad angegeben werden")
            pfad = arg
        i += 1
    return pfad, pflicht


def nur_lesend_oeffnen(pfad):
    return sqlite3.connect(Path(pfad).resolve().as_uri() + "?mode=ro", uri=True)


def zeilenzahlen(verbindung, namen=None):
    """Liefert ({Tabelle: Zeilenzahl}, [alle Tabellen]) ohne SQLite-interne Tabellen.
    Gezaehlt wird nur, was in 'namen' steht (None = alles)."""
    cursor = verbindung.cursor()
    vorhanden = [
        z[0]
        for z in cursor.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type = 'table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
        ).fetchall()
    ]
    ergebnis = {}
    for name in vorhanden:
        if namen is not None and name not in namen:
            continue
        sicherer_name = name.replace('"', '""')
        ergebnis[name] = cursor.execute(f'SELECT COUNT(*) FROM "{sicherer_name}"').fetchone()[0]
    return ergebnis, vorhanden


def live_vergleich(backup_pfad, backup_zahlen):
    """Nur ein Hinweis: Zeilenzahlen der Backup-Tabellen gegen die Live-DB (nur lesend)."""
    if not os.path.isfile(live_datei):
        return
    if Path(live_datei).resolve() == Path(backup_pfad).resolve():
        return
    live_verbindung = None
    try:
        live_verbindung = nur_lesend_oeffnen(live_datei)
        live_zahlen, _ = zeilenzahlen(live_verbindung, set(backup_zahlen))
    except sqlite3.Error as fehler:
        print(f"Hinweis: Live-Datenbank '{live_datei}' war nicht lesbar ({fehler}), kein Vergleich.")
        return
    finally:
        if live_verbindung is not None:
            live_verbindung.close()
    abweichungen = [
        f"{name}: Backup {backup_zahlen[name]}, Live {live_zahlen[name]}"
        for name in backup_zahlen
        if name in live_zahlen and live_zahlen[name] != backup_zahlen[name]
    ]
    if abweichungen:
        print("Hinweis: Zeilenzahlen weichen von der Live-Datenbank ab (Backup evtl. aelter):")
        for zeile in abweichungen:
            print(f"   - {zeile}")
    else:
        print("Hinweis: Zeilenzahlen der geprueften Tabellen stimmen mit der Live-Datenbank ueberein.")


def pruefen(pfad, pflicht):
    if not os.path.isfile(pfad):
        print(f"❌ FEHLER: Die Sicherungsdatei '{pfad}' existiert nicht auf der SSD")
        return EXIT_DATEI_FEHLT

    verbindung = None
    try:
        verbindung = nur_lesend_oeffnen(pfad)
        print(f"\n🔍️ Scanne Backup-Struktur auf Bit-Ebene...")
        ergebnis = verbindung.execute("PRAGMA integrity_check;").fetchall()
        if ergebnis != [("ok",)]:
            print(f"🚨 WARNUNG: Beschädigung im Backup gefunden! Details: {ergebnis}")
            return EXIT_UNGUELTIG
        interessant = set(pflicht) | set(OPTIONALE_TABELLEN)
        zahlen, vorhanden = zeilenzahlen(verbindung, interessant)
    except sqlite3.Error as fehler:
        print(f"🚨 CRITICAL SQL ERROR WÄHREND DES CHECKS: {fehler}")
        return EXIT_UNGUELTIG
    finally:
        if verbindung is not None:
            verbindung.close()

    fehlend = [name for name in pflicht if name not in vorhanden]
    if fehlend:
        print("WARNUNG: Die Sicherung ist intakt, aber es fehlen Pflichttabellen: " + ", ".join(fehlend))
        return EXIT_PFLICHT_FEHLT

    print(f"💎 SUCCESS: Struktur der Sicherung '{pfad}' ist intakt, alle Pflichttabellen sind vorhanden.")
    print("🛡️ Stempel: SQL-INTEGRITY-OK")
    print("   Geprueft: integrity_check und Tabellenbestand. Keine Aussage ueber Aktualitaet oder vollstaendigen Inhalt.")

    for name in pflicht:
        if zahlen.get(name) == 0:
            print(f"Hinweis: Pflichttabelle '{name}' hat 0 Zeilen.")
    fehlende_optionale = [n for n in OPTIONALE_TABELLEN if n not in vorhanden]
    if fehlende_optionale:
        print("Hinweis: Optionale Tabellen nicht vorhanden: " + ", ".join(fehlende_optionale))
    live_vergleich(pfad, {n: zahlen[n] for n in pflicht})
    return EXIT_OK


def main():
    try:
        pfad, pflicht = argumente_lesen(sys.argv[1:])
    except AufrufFehler as fehler:
        print(f"AUFRUFFEHLER: {fehler}")
        print("   Aufruf: python3 136_backup_check.py [Pfad] [--pflicht tabelle1,tabelle2]")
        return EXIT_AUFRUF
    return pruefen(pfad if pfad is not None else backup_datei, pflicht)


if __name__ == "__main__":
    sys.exit(main())
