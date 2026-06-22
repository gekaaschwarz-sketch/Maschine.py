# 019_gesamtgewicht.py
fracht = ["Holz", "Stahl", "Papier", "Glas"]
gewichte = [1500, 2500, 150, 400]

def lkw_kontrolle(artikel, zahlen):
    gesamt = sum(zahlen) # Hier passiert die Magie!

    print("--- LADEPROTOKOLL ---")
    print("Anzahl der Artikel: " + str(len(artikel)))
    print("Gesamtgewicht: " + str(gesamt) + " kg")

    # Sicherheit-Check für den LKW (Limit: 4000 kg)
    if gesamt > 4000:
        print("❌️ STOPP! Der LKW ist überladen!")
    else:
        print("✅️ Fahrt frei: Gewicht im Limit.")

# Funktion aufrufen
lkw_kontrolle(fracht, gewichte)
