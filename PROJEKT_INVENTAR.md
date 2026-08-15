# Offizielles Projekt-Inventar: Maschine.py

Dieses Dokument wurde vollautomatisch generiert.

| Quellcode-Datei | Funktion / Terminal-Überschrift |
| :--- | :--- |
| `002_taschenrechner.py` | Abfrage der Zahlen |
| `003_entscheidung.py` | Fragt Plus oder Minus ab und rechnet zwei eingegebene Zahlen entsprechend |
| `004_logistik_tool.py` | Rechnet ein eingegebenes Gewicht von Pfund in Kilogramm um |
| `005_fehlerschutz.py` | Wie 004, aber mit try/except gegen ungueltige (nicht-numerische) Eingaben abgesichert |
| `006_schleife.py` | Wandelt Pfund in Kilogramm um, wiederholt sich per while-Schleife bis Eingabe 'ende' |
| `007_listen.py` | Legt eine Frachtliste an, fuegt ein Gut hinzu und zeigt Liste sowie erstes Element |
| `008_fracht_manager.py` | Baut interaktiv eine Frachtliste auf, bis der Nutzer 'fertig' eingibt |
| `009_liste_loeschen.py` | Entfernt ein vom Nutzer gewaehltes Gut aus der Frachtliste, falls vorhanden |
| `010_speichern.py` | Schreibt Frachtdaten in eine Textdatei und liest sie anschliessend wieder aus |
| `011_auto_laden.py` | Prüfen, ob die Datei überhaupt existiert |
| `012_super_manager.py` | 1. AUTOMATISCH LADEN |
| `013_funktionen.py` | Definiert eine Begruessungsfunktion, die den eingegebenen Namen anspricht |
| `014_modular.py` | Definiert eine Funktion, die den LKW-Ladungsstatus formatiert anzeigt |
| `015_sicher_löschen.py` | Loescht ein Gut aus der Fracht erst nach expliziter Bestaetigung durch den Nutzer |
| `016_suche.py` | Sucht ein Gut in der Frachtliste und gibt dessen Position aus, falls vorhanden |
| `017_gewichte.py` | Sucht ein Gut in der Liste und gibt das zugehoerige Gewicht ueber den gemeinsamen Index aus |
| `018_warnung.py` | Prueft das Gewicht eines Gutes und warnt, wenn es die 1000-kg-Grenze |
| `019_gesamtgewicht.py` | Summiert das Gesamtgewicht der Fracht und stoppt bei Ueberladung ueber 4000 |
| `020_zoll_rechner.py` | Berechnet den Gesamtzoll aus Frachtgewicht und einem festen Zollsatz pro Kilo |
| `021_sortieren.py` | Sortiert eine Gewichtsliste einmal aufsteigend und einmal absteigend |
| `022_suche_plus.py` | Sucht ein Gut in der Fracht und gibt bei Erfolg zusaetzlich dessen Position aus |
| `023_entladen.py` | Leert die komplette Frachtliste per .clear(), sobald der LKW in Hamburg ankommt |
| `024_sperre.py` | Leert die Fracht nur nach expliziter 'JA'-Bestaetigung durch den Nutzer |
| `025_benutzerfreundlich.py` | Leert die Fracht nach Bestaetigung, wobei .upper() Gross-/Kleinschreibung bei der Eingabe ignoriert |
| `026_woerterbuch.py` | Legt ein Dictionary mit Gewichten an und sucht das Gewicht zu einem eingegebenen Artikel |
| `027_lager_update.py` | Fragt ein neues Gut und Gewicht ab und fuegt es dem Lager-Dictionary hinzu |
| `028_lager_loeschen.py` | Loescht ein vom Nutzer gewaehltes Gut aus dem Lager-Dictionary, falls vorhanden |
| `029_lager_wert.py` | Berechnet Gesamtgewicht und Durchschnittsgewicht aller Positionen im Lager-Dictionary |
| `030_lastverteilung.py` | Berechnet fuer mehrere Ladungen die anteilige Hinterachslast aus Gewicht und Abstand |
| `031_lvp_iteraktiv.py` | Fragt Gewicht und Abstand interaktiv ab und berechnet die zusaetzliche Hinterachslast |
| `032_lvp_warnung.py` | Wie 031, warnt zusaetzlich wenn die Achslast das 6000-kg-Limit ueberschreitet |
| `033_optimierer.py` | Berechnet den maximal zulaessigen Abstand von vorn, um die Achslast-Grenze einzuhalten |
| `034_airbag.py` | Fragt ein Gewicht ab und faengt ungueltige (nicht-numerische) Eingaben per try/except ab |
| `035_endlos_check.py` | Erzwingt per Endlosschleife eine gueltige Zahleneingabe fuer das Gewicht |
| `036_lvp_profi.py` | Nutzt eine wiederverwendbare Eingabefunktion fuer Gewicht und Abstand zur Achslast-Berechnung |
| `037_protokol.py` | Schreibt einen Zeitstempel-Eintrag mit Text ans Ende der Logbuch-Datei (append) |
| `038_final_check.py` | Berechnet die Hinterachslast per sicherer Eingabefunktion und protokolliert das Ergebnis im Logbuch |
| `039_log_lesen.py` | Liest die Logbuch-Datei aus und zeigt ihren Inhalt an, oder meldet wenn sie leer/fehlt |
| `040_log_limit.py` | Zeigt nur die letzten drei Eintraege aus der Logbuch-Datei an |
| `041_logik_check.py` | Fragt ein Gewicht ab, das per Schleife so lange wiederholt wird, bis es positiv ist |
| `042_universal_check.py` | Fragt einen Wert innerhalb eines Min/Max-Bereichs ab, hier genutzt fuer die LKW-Laenge (5 bis 18.75 m) |
| `043_sicheres_log.py` | Prueft eine Achslast im gueltigen Bereich (0-11500 kg) und schreibt das Ergebnis ins Logbuch |
| `044_json_save.py` | Speichert einen Frachtdatensatz als JSON-Datei (frachtbrief.json) |
| `045_json_load.py` | Liest den JSON-Frachtbrief ein und zeigt Fahrer*in, Ladung und Gewicht an |
| `046_json_update.py` | Laedt den JSON-Frachtbrief, aktualisiert das Gewicht und speichert das Ergebnis in fracht.json |
| `047_ip_check.py` | Fragt per Webdienst die aktuelle oeffentliche IP-Adresse ab, um die Internetverbindung zu pruefen |
| `048_flotte.py` | Legt eine Flotten-Liste aus LKW-Dictionaries an und gibt ID sowie Fahrer*in jedes LKW aus |
| `049_flotten_gewicht.py` | Summiert die Gesamtlast aller LKW in der Flotten-Liste |
| `050_jubilaeum.py` | Berechnet Durchschnittslast der Flotte und ermittelt den LKW mit der groessten Last |
| `051_flotte_save.py` | Start |
| `052_flotte_load.py` | 🚛️ FLOTTEN-STATUS AKTUEL |
| `053_flotte_add.py` | 1. Bestehende Datenbank laden |
| `054_namens_check.py` | Deine neues Qualitäts-Format |
| `055_flotte_profi.py` | 1. Deine neue Sicherheits-Funktion |
| `056_last_check.py` | Testlauf |
| `057_kombi_check.py` | Funktion 1: Namens-Check |
| `058_id_schutz.py` | Wir prüfen jede vorhandene ID in der Liste |
| `059_lkw_loeschen.py` | Wir suchen den LKW mit der passenden ID |
| `060_hauptmenue.py` | Erstes interaktives Hauptmenue: zeigt die Flotte an, Loeschen ist noch nicht implementiert (Platzhalter) |
| `061_menue_loeschen.py` | Erweitert das Hauptmenue um eine echte Loeschfunktion fuer einen LKW per ID |
| `062_menue_add.py` | Wächter: Namens-Validierung |
| `063_final_term.py` | Wächter: Namens-Schutz |
| `064_schleifen_fix.py` | Eine neue Liste bauen, die nur die LKWs enthält, die NICHT gelöscht werden sollen |
| `065_profi_term.py` | Fuegt einen neuen LKW hinzu, mit Namens-Validierung und Schutz vor doppelten IDs |
| `066_all_in_one.py` | Kombiniert Anzeigen, Hinzufuegen und eine radikale Loeschfunktion (entfernt alle Eintraege mit gleicher ID) |
| `067_wert_schutz.py` | try fängt ab, wenn der Nutzer Buchstaben statt Zahlen eintippt |
| `068_festung_term.py` | Ergaenzt eine Gewichts-Validierung (0 bis 40000 kg) beim Hinzufuegen eines neuen LKW |
| `069_notaus_term.py` | Wächter 1: Namens-Schutz MIT NOTAUS-SYSTEM! |
| `070_doppel_notaus.py` | Wächter 1: Namens-Schuty MIT NOTAUS-SYSTEM |
| `071_wert_notaus.py` | Wächter 1: Namens-Schuts MIT NOTAUS-SYSTEM! |
| `072_loeschen_profi.py` | Loescht einen LKW erst nach expliziter Ja/Nein-Bestaetigung durch den Nutzer |
| `073_mehrfach_loeschen.py` | Loescht alle LKW-Eintraege mit einer bestimmten ID auf einmal, nach Bestaetigung |
| `074_suche_profi.py` | Option 1: |
| `075_bearbeiten_profi.py` | Sucht einen LKW per ID und aktualisiert dessen Ladungsgewicht interaktiv |
| `076_umregistrieren.py` | Aendert bei einem gefundenen LKW sowohl die ID als auch den Fahrernamen komplett |
| `077_export_profi.py` | Exportiert die komplette Flotte als formatierten Bericht in die Datei speditions_bericht.txt |
| `078_statistik_profi.py` | Berechnet Anzahl, Gesamtgewicht und Durchschnittslast aller LKW in der Flotte |
| `079_sqlite_start.py` | SQLITE-DATENBANK-TRESOR STARTEN |
| `080_tabelle_bau.py` | SQL-TABELLENSTRUKTUR ERSTELLEN |
| `081_daten_rein.py` | LKW-DATEN IN TRESOR LADEN |
| `082_daten_auslesen.py` | \n 🗄️ SQL-DATENBANK: AKTUELLE FLOTTE |
| `083_daten_loeschen.py` | LKW AUS TRESOR LÖSCHEN |
| `084_daten_update.py` | LKW-UPDATE IM TRESOR AKTUALISIEREN |
| `085_kontrolle.py` | FINALER SQL-TRESOR CHECK |
| `086_dynamisch.py` | DYNAMISCHES LKW-UPDATE |
| `087_neuer_lkw.py` | NEUEN LKW REGISTRIEREN |
| `088_suche.py` | SQL-BLITZSUCHE NACH ID |
| `089_super_suche.py` | Sucht in der SQL-Datenbank einen LKW wahlweise per ID oder per Fahrername |
| `090_fehlerschutz.py` | Wie 089, aber bricht das Skript sofort ab, wenn eine ungueltige Menuewahl eingegeben wird |
| `091_sortieren.py` | ⚖️ FLOTTE NACH GEWICHT SORTIERT |
| `092_gewicht_filter.py` | HOCHLAST-FILTER (> 4000 kg) |
| `093_zaehlen.py` | 📊 FLOTTEN-STATISTIK: ANZAHL |
| `094_gesamtgewicht.py` | 📊 FLOTTEN-STATISTIK: GESAMTGEWICHT |
| `095_durchschnitt.py` | 📊 PROFI-STATISTIK & LIMIT |
| `096_hauptprogramm_sql.py` | Erstes SQL-Hauptmenue: zeigt die Flotte aus der Datenbank an, nur Anzeigen und Beenden moeglich |
| `097_hauptprogramm_insert.py` | Erweitert das SQL-Hauptmenue um das Einfuegen eines neuen LKW in die Datenbank |
| `098_hauptprogramm_delete.py` | Erweitert das SQL-Hauptmenue um das Loeschen eines LKW per ID (mit Abbruch-Option 'x') |
| `099_hauptprogramm_update.py` | Erweitert das SQL-Hauptmenue um das Aktualisieren der LKW-Last, abgesichert per try/except |
| `107_zweig_feature.py` | 🌿 FEATURE-BRANCH: SUPER-STATISTIK |
| `113_kunden_tabelle.py` | 👥 SQL-KUNDEN-ZENTRALE v1.0 |
| `114_sql_join.py` | 📊 COMBINED DISPO-REPORT (SQL JOIN) |
| `115_optimierung.py` | ⚡️ SQL-HOCHGESCHWINDIGKEITS-CHECK |
| `117_join_schutz.py` | 🛡️ SQL-JOIN-SCHUTZWALL v1.0 |
| `118_datenbank_saeubern.py` | 🧹 SQL-DATENBANK-BEREINIGUNG |
| `119_kunde_update.py` | 👥 SQL-KUNDEN-DISPO-UPDATE |
| `120_csv_export.py` | 📥️ SQL TRESOR-EXPORT NACH EXCEL |
| `121_csv_import.py` | 📥️ SQL TRESOR-IMPORT AUS EXCEL |
| `122_import_schutz.py` | 🛡️ SQL-DUPLIKAT-SCHUTZWALL v1.0 |
| `123_tresor_reset.py` | 🧹 KUNDEN-TRESOR KASSIEREN (RESET) |
| `124_duplikat_test.py` | 🔬 DER GROSSE DUPLIKAT-HÄRTETEST |
| `125_like_suche.py` | 🔍️ SQL-SMART-SUCHE (WILD-CARDS) |
| `126_multi_suche.py` | 🗺️ MULTI-SUCHE: KUNDE & FLOTTE |
| `127_sql_schutze.py` | 🛡️ SQL-KRISEN-SCHUTZWALL v1.0 |
| `128_sql_transaktion.py` | 🛡️ SQL-TRANSAKTION-WALL (ROLLBACK) |
| `129_sql_backup.py` | 💾 AUTOMATISCHES DATEN-BACKUP |
| `130_backup_clean.py` | 🧹 BACKUP-SPEICHER-BEREINIGUNG |
| `131_sql_logbuch.py` | 📝 SYSTEM-LOGBUCH (SQL-Tabelle) |
| `132_log_rotator.py` | 🧹 AUTOMATISCHER SQL-LOG-ROTATOR |
| `133_daten_bereinigung.py` | 🧼 SQL-KUNDEN-DATENBEREINIGUNG |
| `134_json_export.py` | SQL-TRESOR-EXPORT NACH JSON |
| `135_json_import.py` | 📥️ SQL TRESOR-IMPORT AUS JSON |
| `136_backup_check.py` | 🛡️ AUTOMATISCHE BACKUP-TÜV-CHECK |
| `137_suche_benchmark.py` | ⏱️ SQL-PERFORMANCE-BENCHMARK |
| `138_index_tuning.py` | ⚙️ AUTOMATISCHES SQL-INDEX-TUNING |
| `139_sql_injection_schutz.py` | 🛡️ SQL-INJECTION-SCHUTZWALL v1.0 |
| `140_database_vacuum.py` | 🧹 SQL-DATENBANK-VAKUUMIERUNG |
| `141_sql_archiv.py` | 🗄️ AUTOMATISCHE TABELLEN-ARCHIVIERUNG |
| `142_sql_verschluesselung.py` | 🔐 AUTOMATISCHE SQL-VERSCHLÜSSELUNG |
| `143_sql_entschluesselung.py` | 🔓️ AUTOMATISCHER KRYPTO-ABGLEICH |
| `144_error_logger.py` | 🚨 AUTOMATISCHER SQL-ERROR-LOGGER |
| `145_sql_restore.py` | 🚒 AUTOMATISCHES SQL-RESTORE-MODUL |
| `146_table_cloner.py` | 🔏 AUTOMATISCHER SQL-TABELLEN-KLON |
| `147_column_extension.py` | ⚙️ SQL-TABELLEN-ERWEITERUNG (ALTER) |
| `148_exclusive_lock.py` | 🔒️ EXKLUSIVE SQL-TRANSAKTIONS-SPERRE |
| `149_table_rename.py` | ⚙️ SQL-TABELLEN-UMBENENNUNG (RENAME) |
| `150_table_truncate.py` | 🧼 AUTOMATISCHE TABELLEN-LEERUNG |
| `151_table_drop.py` | 🗑️ AUTOMATISCHES SQL-TABELLEN-DROP |
| `152_cross_db_copy.py` | 📑 CROSS-DATABASE TABELLEN-KOPIE |
| `153_db_analyze.py` | 📊 AUTOMATISCHE SQL-VOLLANALYSE |
| `154_query_explain.py` | 🔬 SQL-ABFRAGE-PLAN-ANALYSE (EXPLAIN) |
| `155_table_info.py` | 🧬 AUTOMATISCHE TABELLEN-DNA-PRÜFUNG |
| `156_index_info.py` | 🔬 AUTOMATISCHE INDEX-DNA-PRÜFUNG |
| `157_list_tables.py` | 📂 AUTOMATISCHE TABELLEN-AUFLISTUNG |
| `158_column_count.py` | 🔬 AUTOMATISCHE SPALTEN-ZÄHLUNG |
| `159_index_count.py` | 🔬 AUTOMATISCHE INDEX-ZÄHLUNG |
| `160_scan_guard.py` | 🛡️ AUTOMATISCHER TABELLEN-SCAN-WÄCHTER |
| `161_create_lkw_index.py` | ⚡️ AUTOMATISCHE LKW-INDEX-SCHMEIDE |
| `162_drop_lkw_index.py` | 🗑️ AUTOMATISCHE INDEX-VERNICHTUNG |
| `163_table_snapshot.py` | 📸 AUTOMATISIERTER TABELLEN-SNAPSHOT |
| `164_data_restore.py` | 🛡️ AUTOMATISCHE DATEN-WIEDERHERSTELLUNG |
| `165_add_column.py` | ⚙️ AUTOMATISCHE SPALTEN-ERWEITERUNG |
| `166_rename_column.py` | ⚙️ AUTOMATISCHE SPALTEN-UMBENENNUNG |
| `167_rename_table.py` | ⚙️ AUTOMATISCHE TABELLEN-UMBENENNUNG |
| `168_drop_table.py` | 🗑️ AUTOMATISCHE TABELLEN-VERNICHTUNG |
| `169_vacuum_db.py` | ⚙️ AUTOMATISCHE DATENBANK-KOMPRESSION |
| `170_db_size.py` | 📊 AUTOMATISCHE DATENBANK-MESSUNG |
| `171_quick_check.py` | 🛡️ AUTOMATISCHER SQL-SCHNELL-CHECK |
| `172_table_lock.py` | 🔒️ AUTOMATISCHE SYSTEM-SPERRUNG |
| `173_table_unlock.py` | 🔓️ AUTOMATISCHE SYSTEM-ENTRIEGELUNG |
| `174_table_lock_read.py` | 📖 AUTOMATISCHE LESE-SPERRUNG |
| `175_table_lock_write.py` | 📝 AUTOMATISCHE SCHREIB-SPERRUNG |
| `176_busy_timeout.py` | 🛡️ AUTOMATISCHE TIMEOUT-SICHERUNG |
| `177_transaction_timeout.py` | 🔒 TRANSAKTIONS-SPERRE MIT TIMEOUT-TEST |
| `178_backup_rotation.py` | 🔄 AUTOMATISIERTE BACKUP-ROTATION |
| `179_db_export_csv.py` | 📊 AUTOMATISIERTER CO2-CSV-EXPORT |
| `180_integrity_check.py` | 🔍 AUTOMATISIERTER DATENBANK-GESUNDHEITSCHECK |
| `189_generate_inventory.py` | 📋 AUTOMATISCHES PROJEKT-INVENTAR |
| `190_find_gaps.py` | 🔎 LÜCKEN-FINDER IM PROJEKT-INVENTAR |
| `kunden_modul_183.py` | Kernfunktionen fuer die Kundenverwaltung: Kunde anlegen (mit Duplikatschutz) und Kunde per Namen suchen |
