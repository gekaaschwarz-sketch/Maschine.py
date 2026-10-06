# Kernfunktionen fuer die Flottenverwaltung: LKW anlegen (mit Duplikatschutz), suchen, auflisten, loeschen und Last aktualisieren

from typing import Optional, List
import sqlite3


DB_TABLE_LKW = "fleet_trucks"


class LKW:
    """Repraesentation eines LKW-Datensatzes als einfacher DTO (datenuebertragungsobjekt)."""

    def __init__(self, id: str, fahrer_in: str, last):
        # Keine Typumwandlung hier; Hauptprogramm prueft Datentypen ggf.
        self.id = id
        self.fahrer_in = fahrer_in
        self.last = last

    def __repr__(self) -> str:
        # ASCII-only Repraesentation
        return f"LKW(id={self.id!r}, fahrer_in={self.fahrer_in!r}, last={self.last!r})"


class FlottenVerwaltung:
    """
    FlottenVerwaltung kapselt CRUD-Operationen fuer die Tabelle fleet_trucks.

    Verhalten:
    - INSERT prueft vorab auf vorhandene ID und wirft ValueError bei Duplikat.
    - SELECTs benutzen explizit die Spaltenliste (id, fahrer_in, last).
    - UPDATE/DELETE committen nur, wenn rowcount > 0; sonst wird rollback ausgefuehrt.
    """

    def __init__(self, db_pfad: str):
        """
        :param db_pfad: Pfad zur SQLite-Datenbankdatei.
        """
        self.db_pfad = db_pfad

    def hinzufuegen(self, id: str, fahrer_in: str, last) -> bool:
        """
        Neuen LKW anlegen.

        :param id: LKW-ID
        :param fahrer_in: Fahrer_in-Name
        :param last: Last-Wert (unveraendert durchgereicht)
        :return: True bei Erfolg
        :raises ValueError: wenn die ID bereits existiert
        """
        conn = sqlite3.connect(self.db_pfad)
        try:
            cur = conn.cursor()
            # Vorabpruefung
            cur.execute(f"SELECT id FROM {DB_TABLE_LKW} WHERE id = ?", (id,))
            if cur.fetchone() is not None:
                raise ValueError(f"LKW mit id={id} existiert bereits.")
            try:
                cur.execute(
                    f"INSERT INTO {DB_TABLE_LKW} (id, fahrer_in, last) VALUES (?, ?, ?)",
                    (id, fahrer_in, last),
                )
                conn.commit()
                return True
            except Exception:
                conn.rollback()
                raise
        finally:
            conn.close()

    def suchen(self, id: str) -> Optional[LKW]:
        """
        LKW nach ID suchen.

        :param id: LKW-ID
        :return: LKW-Objekt oder None
        """
        conn = sqlite3.connect(self.db_pfad)
        try:
            cur = conn.cursor()
            cur.execute(f"SELECT id, fahrer_in, last FROM {DB_TABLE_LKW} WHERE id = ?", (id,))
            row = cur.fetchone()
            if row:
                return LKW(row[0], row[1], row[2])
            return None
        finally:
            conn.close()

    def alle(self) -> List[LKW]:
        """
        Alle LKWs zurueckgeben.

        :return: Liste von LKW-Objekten
        """
        conn = sqlite3.connect(self.db_pfad)
        try:
            cur = conn.cursor()
            cur.execute(f"SELECT id, fahrer_in, last FROM {DB_TABLE_LKW}")
            rows = cur.fetchall()
            return [LKW(r[0], r[1], r[2]) for r in rows]
        finally:
            conn.close()

    def loeschen(self, id: str) -> bool:
        """
        LKW mit gegebener ID loeschen.

        Commit nur, wenn rowcount > 0. Bei 0 wird rollback ausgefuehrt.

        :param id: LKW-ID
        :return: True, wenn eine Zeile geloescht wurde, sonst False
        """
        conn = sqlite3.connect(self.db_pfad)
        try:
            cur = conn.cursor()
            try:
                cur.execute(f"DELETE FROM {DB_TABLE_LKW} WHERE id = ?", (id,))
                affected = cur.rowcount
                if affected > 0:
                    conn.commit()
                    return True
                else:
                    conn.rollback()
                    return False
            except Exception:
                conn.rollback()
                raise
        finally:
            conn.close()

    def last_aktualisieren(self, id: str, neue_last) -> bool:
        """
        Last fuer einen LKW aktualisieren.

        Commit nur, wenn rowcount > 0. Bei 0 wird rollback ausgefuehrt.

        :param id: LKW-ID
        :param neue_last: neue Last (unveraendert weitergereicht)
        :return: True, wenn eine Zeile geaendert wurde, sonst False
        """
        conn = sqlite3.connect(self.db_pfad)
        try:
            cur = conn.cursor()
            try:
                cur.execute(
                    f"UPDATE {DB_TABLE_LKW} SET last = ? WHERE id = ?",
                    (neue_last, id),
                )
                changed = cur.rowcount
                if changed > 0:
                    conn.commit()
                    return True
                else:
                    conn.rollback()
                    return False
            except Exception:
                conn.rollback()
                raise
        finally:
            conn.close()


if __name__ == "__main__":
    # Hinweis: dieses Modul ist nicht als Script gedacht.
    # Importiere FlottenVerwaltung und verwende es im Hauptprogramm.
    print("Dieses Modul enthaelt Klassen fuer die Flottenverwaltung. Importiere und benutze FlottenVerwaltung im Hauptprogramm.")