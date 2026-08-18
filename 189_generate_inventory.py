import os

LINIE = "=" * 45

print("\n" + LINIE)
print("--- 📋 AUTOMATISCHES PROJEKT-INVENTAR ---")
print(LINIE)

verzeichnis = "."
inventar_datei = "PROJEKT_INVENTAR.md"

print(f"\n⚡ Starte optimierte Struktur-Analyse im Verzeichnis '{verzeichnis}'...")

try:
    relevante_dateien = []

    for wurzel, ordner, dateien in os.walk(verzeichnis):
        # __pycache__-Ordner komplett ueberspringen (nur Cache-Muell)
        if "__pycache__" in wurzel:
            continue

        for datei in dateien:
            if datei.endswith(".py") and (datei[:3].isdigit() or datei.startswith("kunden_modul")):
                pfad = os.path.join(wurzel, datei)
                pfad = pfad.replace("./", "", 1)  # fuehrendes "./" entfernen
                relevante_dateien.append(pfad)

    relevante_dateien.sort()
    print(f"🔍 {len(relevante_dateien)} Quellcode-Dateien für das Inventar lokalisiert.")

    with open(inventar_datei, "w", encoding="utf-8") as datei_objekt:
        datei_objekt.write("# Offizielles Projekt-Inventar: Maschine.py\n\n")
        datei_objekt.write("Dieses Dokument wurde vollautomatisch generiert.\n\n")
        datei_objekt.write("| Quellcode-Datei | Funktion / Terminal-Überschrift |\n")
        datei_objekt.write("| :--- | :--- |\n")

        for pfad in relevante_dateien:
            beschreibung = "Keine Beschreibung extrahierbar."
            try:
                with open(pfad, "r", encoding="utf-8") as f:
                    for _ in range(15):
                        zeile = f.readline()
                        if not zeile:
                            break
                        zeile = zeile.strip()

                        if zeile.startswith("#") and zeile.strip().endswith(".py"):
                            continue

                        if "print(" in zeile and "---" in zeile:
                            inhalt = zeile.replace('print("', '').replace('")', '')
                            inhalt = inhalt.replace("print('", "").replace("')", "")
                            beschreibung = inhalt.replace("---", "").strip()
                            break
                        elif zeile.startswith("#") and not zeile.startswith("#!") and "====" not in zeile:
                            beschreibung = zeile.lstrip("# ").strip()
                            break
            except Exception:
                beschreibung = "🚨 Fehler beim Einlesen der Datei."

            datei_objekt.write(f"| `{pfad}` | {beschreibung} |\n")

    print(f"💎 SUCCESS: Das intelligente Inventar '{inventar_datei}' wurde generiert!")

except Exception as fehler:
    print(f"🚨 FEHLER BEIM GENERIEREN DES INVENTARS: {fehler}")

print("\n" + LINIE)
print("⚙️ Inventar-Modul abgeschlossen.")
print(LINIE)