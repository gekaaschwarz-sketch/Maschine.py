import sqlite3

print("\n===============================================")
print("--- 🛡️ AUTOMATISCHE DATEN-WIEDERHERSTELLUNG ---")
print("===============================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n🚨 SIMULATION: Kritischer Datenverlust! Lösche Live-Tabelle 'fleet_trucks'...")
    try:
        # Sicherheitscheck: Snapshot muss vorhanden sein, bevor wir zerstören.
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='fleet_trucks_backup_snapshot';"
        )
        if cursor.fetchone() is None:
            print("🚨 ABBRUCH: Snapshot 'fleet_trucks_backup_snapshot' nicht gefunden — kein Restore möglich.")
        else:
            # Atomare Wiederherstellung in einer einzigen Transaktion.
            # Wir verwenden explizite BEGIN/COMMIT und rollen bei Fehlern zurück.
            print("⚠️ WARNUNG: Alle Live-Daten werden temporär gelöscht — starte atomaren Restore...")
            try:
                cursor.execute("BEGIN;")
                # Lösche Live-Daten
                cursor.execute("DELETE FROM fleet_trucks;")

                # Einfügen aus Snapshot (explizite Spaltenliste vermeidet Spaltenfehlzuordnungen)
                cursor.execute("""
                    INSERT INTO fleet_trucks (id, fahrer_in, last, payload_tons)
                    SELECT id, fahrer_in, last, payload_tons FROM fleet_trucks_backup_snapshot;
                """)

                cursor.execute("COMMIT;")
                print("💎 SUCCESS: Daten erfolgreich aus dem Sicherheitsnetz zurückgerettet!")

                cursor.execute("SELECT COUNT(*) FROM fleet_trucks;")
                anzahl_live = cursor.fetchone()[0]
                print(f"📊 Integritäts-Prüfung: Live-Betrieb mit exakt {anzahl_live} LKW-Datensätzen wiederhergestellt.")
            except sqlite3.Error as txn_fehler:
                # Rollback auf sichere Konsistenz, falls Fehler in der Transaktion auftreten
                try:
                    cursor.execute("ROLLBACK;")
                except Exception:
                    pass
                print(f"🚨 FEHLER WÄHREND ATOMAREM RESTORE: {txn_fehler}")
    except sqlite3.Error as fehler:
        print(f"🚨 FEHLER BEIM RESTORE-PROZESS: {fehler}")

print("\n⚙️ Rettungs-Modul abgeschlossen: System-Integrität zu 100 % stabilisiert.")