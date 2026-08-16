import json

def pruefe_id_frei(neue_id):
    try:
        with open("flotten_datenbank.json", "r") as f:
            flotte = json.load(f)

        # Wir prüfen jede vorhandene ID in der Liste
        for lkw in flotte:
            if lkw["ID"] == neue_id:
                return False # ID ist schon vergeben!
        return True # ID ist frei!
    except FileNotFoundError:
        return True

# Testlauf
print("--- SYSTEM-CHECK: EINDEUTIGE ID ---")
test_id = input("Neue LKW_ID eingeben (z.B. HH-01): ")

if pruefe_id_frei(test_id):
    print(f"✅️ Die ID {test_id} ist frei und kann genutzt werden.")
else:
    print(f"❌️ FEHLER: Die ID {test_id} existiert bereits in der Datenbank!")
