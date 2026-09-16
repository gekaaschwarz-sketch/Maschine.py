# Historische Schema-Migrationen

Die folgenden Skripte dokumentieren bereits durchgeführte Änderungen am
SQLite-Schema. Sie gehören nicht zum aktiven Migrations-Sweep und dürfen nicht
erneut gegen die aktuelle Produktionsdatenbank ausgeführt werden.

## 165_add_column.py

Datei: `08_wartung/165_add_column.py`

Historischer Schritt:

- Tabelle: `lkw_flotte`
- Hinzugefügte Spalte: `nutzlast_tonnen`
- Defaultwert: `12`

Anschließender historischer Zustand:

- `nutzlast_tonnen` wurde in der folgenden Migration zu `payload_tons`
  umbenannt.
- Die aktuelle Tabelle `fleet_trucks` enthält bereits `payload_tons` mit
  Defaultwert `12`.

Ist-Zustand-Nachweis:

```bash
grep -RniE "nutzlast_tonnen|payload_tons" --include="*.py" .
```

Der Check zeigt, dass die aktuellen Restore- und Transaktionsskripte
`payload_tons` verwenden. Zusätzlich wurde die aktuelle Tabellenstruktur mit
`PRAGMA table_info(fleet_trucks)` geprüft; dort ist `payload_tons` mit dem
Defaultwert `12` vorhanden.

## 166_rename_column.py

Datei: `08_wartung/166_rename_column.py`

Historischer Schritt:

- Tabelle: `lkw_flotte`
- Umbenennung: `nutzlast_tonnen` → `payload_tons`

Ist-Zustand-Nachweis:

```bash
python3 -c "import sqlite3; db = sqlite3.connect('speditions_tresor.db'); print(db.execute('PRAGMA table_info(fleet_trucks)').fetchall()); db.close()"
```

Der Check zeigt, dass `payload_tons` in der aktuellen Tabelle `fleet_trucks`
bereits vorhanden ist. `nutzlast_tonnen` ist nicht mehr der aktuelle
Spaltenname.

## 167_rename_table.py

Datei: `08_wartung/167_rename_table.py`

Historischer Schritt:

- Umbenennung der Tabelle: `lkw_flotte` → `fleet_trucks`

Ist-Zustand-Nachweis:

```bash
python3 -c "import sqlite3; db = sqlite3.connect('speditions_tresor.db'); print(db.execute('PRAGMA table_info(fleet_trucks)').fetchall()); db.close()"
```

Der Check bestätigt, dass `fleet_trucks` als aktuelle Tabelle vorhanden ist.
`lkw_flotte` existiert in der aktuellen Produktionsdatenbank nicht mehr.
Ein Such-/Ersetzungs-Diff würde deshalb fälschlicherweise zu
`ALTER TABLE fleet_trucks RENAME TO fleet_trucks` führen.

## 168_drop_table.py

Datei: `08_wartung/168_drop_table.py`

Historischer Schritt:

- Aufräumen der alten Snapshot-Tabelle:
  `lkw_flotte_backup_snapshot`

Ist-Zustand-Nachweis:

```bash
python3 -c "import sqlite3; db = sqlite3.connect('speditions_tresor.db'); print(db.execute(\"SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%backup_snapshot%'\").fetchall()); db.close()"
```

Der Check zeigt, dass ausschließlich
`fleet_trucks_backup_snapshot` existiert. Die alte Tabelle
`lkw_flotte_backup_snapshot` ist nicht mehr vorhanden.

Die aktuelle Datei enthält daher bewusst weiterhin:

```sql
DROP TABLE IF EXISTS lkw_flotte_backup_snapshot;
```

Bei einer Ausführung ist diese Anweisung ein No-Op. Ein Ersetzen des Namens
durch `fleet_trucks_backup_snapshot` würde dagegen die aktuell verwendete
Snapshot-Tabelle löschen und ist deshalb keine reine Migrationsbereinigung.

## Status

Die Dateien 165, 166, 167 und 168 werden als historische Lern- bzw.
Migrationsskripte beibehalten. Sie werden nicht per einfachem
`lkw_flotte`-zu-`fleet_trucks`-Such-/Ersetzungs-Diff angepasst und nicht
erneut gegen die aktuelle Produktionsdatenbank ausgeführt.
