import requests

def vpn_check():
    print("--- SYSTEM-SICHERCHEITS-CHECK ---")
    try:
        # Hier wird die Webseite nach der IP gefragt
        response = requests.get('https//ipify.org', timeout=5)
        daten = response.json()
        aktuelle_ip = daten['ip']

        print("Deine IP-Adresse ist: " + aktuelle_ip)
        print("✅️ Verbindung zum Internet steht.")

    except:
        print("❌️ FEHLER: Internet-Abfrage fehlgeschlagen oder VPN blockirt!")

# Start
vpn_check()
