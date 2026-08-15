import re
from collections import Counter

INVENTAR_DATEI = "PROJEKT_INVENTAR.md"

print("\n" + "=" * 45)
print("--- 🔎 LÜCKEN-FINDER IM PROJEKT-INVENTAR ---")
print("=" * 45)

luecken = []
alle_eintraege = []  # (dateiname, beschreibung) fuer die Duplikat-Pruefung

try:
    with open(INVENTAR_DATEI, "r", encoding="utf-8") as f:
        zeilen = f.readlines()

    for zeile in zeilen:
        if not zeile.startswith("| `"):
            continue

        teile = zeile.strip().split("|")
        if len(teile) < 3:
            continue

        dateiname = teile[1].strip().strip("`")
        beschreibung = teile[2].strip()

        alle_eintraege.append((dateiname, beschreibung))

        # Check 1: Beschreibung ist (fast) identisch mit dem Dateinamen
        name_ohne_endung = dateiname.replace(".py", "")
        if beschreibung == dateiname or beschreibung == name_ohne_endung:
            luecken.append((dateiname, "identisch mit Dateiname"))

        # Check 2: Fallback-Text wurde nie ersetzt
        if "Keine Beschreibung extrahierbar" in beschreibung:
            luecken.append((dateiname, "keine Beschreibung gefunden"))

    # Check 3: Beschreibung kommt mehrfach identisch vor (NEU)
    beschreibungs_zaehler = Counter(beschr for _, beschr in alle_eintraege)
    bereits_erfasst = {d for d, _ in luecken}

    for dateiname, beschreibung in alle_eintraege:
        if beschreibungs_zaehler[beschreibung] > 1 and dateiname not in bereits_erfasst:
            luecken.append((dateiname, f"Duplikat ({beschreibungs_zaehler[beschreibung]}x: '{beschreibung}')"))

    print(f"\n🚨 {len(luecken)} Dateien mit verdaechtiger Beschreibung gefunden:\n")
    for i, (name, grund) in enumerate(luecken, start=1):
        print(f"  {i}. {name}  -->  {grund}")

    with open("LUECKEN_LISTE.txt", "w", encoding="utf-8") as f:
        for name, grund in luecken:
            f.write(f"{name} | {grund}\n")

    print(f"\n💾 Liste gespeichert in 'LUECKEN_LISTE.txt' ({len(luecken)} Eintraege).")

except FileNotFoundError:
    print(f"🚨 FEHLER: '{INVENTAR_DATEI}' nicht gefunden. Erst 189_generate_inventory.py ausführen.")

print("\n" + "=" * 45)