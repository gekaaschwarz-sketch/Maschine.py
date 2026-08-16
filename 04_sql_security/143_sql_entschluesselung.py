import sqlite3
import hashlib

print("\n==========================================")
print("--- 🔓️ AUTOMATISCHER KRYPTO-ABGLEICH ---")
print("==========================================")

eingabe_passwort = "Festung_Hamburg_2026!"

eingabe_hash = hashlib.sha256(eingabe_passwort.encode()).hexdigest()

with sqlite3.connect("speditions_tresor.db") as verbindung:
    cursor = verbindung.cursor()

    print("\n🔍️ Hole verriegelten Sicherheits-Schlüssel aus dem Tresor...")
    cursor.execute("SELECT geheim_code FROM geheim_tresor WHERE schluessel_typ = 'Master-SHA256'")
    ergebnis = cursor.fetchone()

    if ergebnis:
        gespeicherter_hash = ergebnis[0]

        print("⚡️ Vergleiche digitale Signaturen auf Bit-Ebene...")
        if eingabe_hash == gespeicherter_hash:
            print("\n🔓️ ACCESS GRANTED: Passwort korrekt! Stahlschrank geöffnet!")
            print("🚛 Willkommen im System der Hamburger Spedition, Valentin.")
        else:
            print("\n🚨 ACCESS DENIED: Falsches Passwort! System sperrt den Zugriff!")
    else:
        print("❌ FEHLER: Kein Master-Schlüssel in der Datenbank gefunden!")

print("\n⚙️ Krypto-Abgleich abgeschlossen: Zugriffskontrolle beendet.")