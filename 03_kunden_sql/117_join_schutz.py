import sqlite3

print("\n=========================================")
print("--- 🛡️ SQL-JOIN-SCHUTZWALL v1.0 ---")
print("=========================================")

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    cursor.execute("INSERT INTO kunden (name, zugeordneter_lkw) VALUES ('Geister-Fracht GmbH', 'HH-NULL')")
    verbindung.commit()

    cursor.execute("""
        SELECT kunden.name, kunden.zugeordneter_lkw, lkw_flotte.fahrer_in
        FROM kunden
        LEFT JOIN lkw_flotte ON kunden.zugeordneter_lkw = lkw_flotte.id
    """)
    bericht_daten = cursor.fetchall()

    print("\n📋️ KONTROLIERTER DISPO-BERICHT:")
    for zeile in bericht_daten:
        kunde_name = zeile[0]
        lkw_id = zeile[1]
        fahrer =zeile[2]

        if fahrer is None:
            print(f"⚠️ ACHTUNG: {kunde_name} hat ungültige LKW-ID ({lkw_id})! Keinen Fahrer zugeordnet!")
        else:
            print(f"Firma: {kunde_name} ➡️ LKW: {lkw_id} ➡️ Crew: {fahrer}")