import re

INVENTAR_DATEI = "PROJEKT_INVENTAR.md"

print("\n" + "=" * 45)
print("--- 🔎 LÜCKEN-FINDER IM PROJEKT-INVENTAR ---")
print("=" * 45)

luecken = []

try:
    with open(INVENTAR_DATEI, "r", encoding="utf-8") as f:
        zeilen = f.readlines()

    for zeile in zeilen:
        if not zeile.startswith("| `"):
            continue  # überspringt Kopfzeilen/Trennlinien

        # Zeile hat Format: | `dateiname.py` | Beschreibung |
        teile = zeile.strip().split("|")
        if len(teile) < 3:
            continue

        dateiname = teile[1].strip().strip("`")
        beschreibung = teile[2].strip()

        # Verdächtig: Beschreibung ist (fast) identisch mit dem Dateinamen
        name_ohne_endung = dateiname.replace(".py", "")
        if beschreibung == dateiname or beschreibung == name_ohne_endung:
            luecken.append(dateiname)

    print(f"\n🚨 {len(luecken)} Dateien ohne echte Beschreibung gefunden:\n")
    for i, name in enumerate(luecken, start=1):
        print(f"  {i}. {name}")

    # Liste zusätzlich in eine Datei schreiben, zum Abhaken
    with open("LUECKEN_LISTE.txt", "w", encoding="utf-8") as f:
        for name in luecken:
            f.write(name + "\n")

    print(f"\n💾 Liste gespeichert in 'LUECKEN_LISTE.txt' ({len(luecken)} Einträge).")

except FileNotFoundError:
    print(f"🚨 FEHLER: '{INVENTAR_DATEI}' nicht gefunden. Erst 189_generate_inventory.py ausführen.")

print("\n" + "=" * 45)