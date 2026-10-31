# 129_sql_backup.py

import os
import sqlite3
import sys
import tempfile
from pathlib import Path

print("\n=========================================")
print("--- 💾 AUTOMATISCHES DATEN-BACKUP ---")
print("=========================================")

quell_datei = "speditions_tresor.db"
ziel_datei = "speditions_tresor_BACKUP.db"

EXIT_OK = 0
EXIT_QUELLE_FEHLT = 1
EXIT_FEHLER = 2


def tabellen_zeilenzahlen(verbindung):
    """Liefert {Tabellenname: Zeilenzahl} ohne SQLite-interne Tabellen."""
    cursor = verbindung.cursor()
    namen = [
        zeile[0]
        for zeile in cursor.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type = 'table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
        ).fetchall()
    ]
    ergebnis = {}
    for name in namen:
        sicherer_name = name.replace('"', '""')
        ergebnis[name] = cursor.execute(
            f'SELECT COUNT(*) FROM "{sicherer_name}"'
        ).fetchone()[0]
    return ergebnis


def sicherung_erstellen(quelle, ziel):
    """
    Erstellt die Sicherung mit der SQLite-Backup-API in eine eindeutige
    temporaere Datei, prueft sie und ersetzt erst danach das alte Backup.
    Bei jedem Fehler bleibt das bisherige Backup unveraendert.
    """
    quell_pfad = Path(quelle).resolve()
    ziel_pfad = Path(ziel).resolve()

    fd, temp_name = tempfile.mkstemp(
        prefix=ziel_pfad.name + ".", suffix=".tmp", dir=str(ziel_pfad.parent)
    )
    os.close(fd)
    temp_pfad = Path(temp_name)

    quell_verbindung = None
    temp_verbindung = None
    try:
        quell_verbindung = sqlite3.connect(quell_pfad.as_uri() + "?mode=ro", uri=True)
        temp_verbindung = sqlite3.connect(str(temp_pfad))
        quell_verbindung.backup(temp_verbindung)

        ergebnis = temp_verbindung.execute("PRAGMA integrity_check").fetchall()
        if ergebnis != [("ok",)]:
            raise RuntimeError(f"integrity_check der neuen Sicherung: {ergebnis}")

        zahlen_quelle = tabellen_zeilenzahlen(quell_verbindung)
        zahlen_backup = tabellen_zeilenzahlen(temp_verbindung)
        if zahlen_quelle != zahlen_backup:
            raise RuntimeError(
                f"Tabellen/Zeilenzahlen weichen ab: Quelle={zahlen_quelle}, Backup={zahlen_backup}"
            )

        temp_verbindung.close()
        temp_verbindung = None
        quell_verbindung.close()
        quell_verbindung = None

        os.replace(temp_pfad, ziel_pfad)
        return zahlen_backup
    except BaseException:
        if temp_verbindung is not None:
            temp_verbindung.close()
            temp_verbindung = None
        if quell_verbindung is not None:
            quell_verbindung.close()
            quell_verbindung = None
        if temp_pfad.exists():
            temp_pfad.unlink()
        raise
    finally:
        if temp_verbindung is not None:
            temp_verbindung.close()
        if quell_verbindung is not None:
            quell_verbindung.close()


def main():
    if not os.path.exists(quell_datei):
        print(f"⚠️ FEHLER: Die Datei '{quell_datei}' wurde nicht gefunden! Kein Backup möglich.")
        return EXIT_QUELLE_FEHLT

    print(f"🔍️ Stamm-Tresor '{quell_datei}' gefunden.")
    try:
        zahlen = sicherung_erstellen(quell_datei, ziel_datei)
    except Exception as fehler:
        print(f"🚨 KRITISCHER DATEI-FEHLER: {fehler}")
        print("Hinweis: Ein vorhandenes Backup wurde nicht veraendert.")
        return EXIT_FEHLER

    print("\n💾 SUCCESS: Vollautomatisches Backup erfolgreich geschmiedet")
    print(f"📁 Sicherungskopie liegt bereit als: '{ziel_datei}'")
    print("Geprueft: integrity_check ok, Tabellenliste und Zeilenzahlen stimmen mit der Quelle ueberein.")
    print("   (Das ist kein vollstaendiger Inhaltsvergleich.)")
    for name, anzahl in zahlen.items():
        print(f"   - {name}: {anzahl} Zeilen")
    return EXIT_OK


if __name__ == "__main__":
    code = main()
    print("\n⚙️ Backup-Modul abgeschlossen: Daten für den Ernstfall gesichert." if code == EXIT_OK
          else "\n⚙️ Backup-Modul beendet: KEIN neues Backup erstellt.")
    sys.exit(code)