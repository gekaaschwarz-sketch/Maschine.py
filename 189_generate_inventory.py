import os

LINIE = "=" * 45

print("\n" + LINIE)
print("--- 📋 AUTOMATISCHES PROJEKT-INVENTAR ---")
print(LINIE)

verzeichnis = "."
inventar_datei = "PROJEKT_INVENTAR.md"

print(f"\n⚡ Starte optimierte Struktur-Analyse im Verzeichnis '{verzeichnis}'...")

try:
    alle_dateien = os.listdir(verzeichnis)
    relevante_dateien = []
    
    for datei in alle_dateien:
        # Wir nehmen nummerierte Lektionen UND das produktive Kundenmodul auf
        if datei.endswith(".py") and (datei[:3].isdigit() or datei.startswith("kunden_modul")):
            relevante_dateien.append(datei)
            
    relevante_dateien.sort()
    print(f"🔍 {len(relevante_dateien)} Quellcode-Dateien für das Inventar lokalisiert.")
    
    with open(inventar_datei, "w", encoding="utf-8") as datei_objekt:
        datei_objekt.write("# Offizielles Projekt-Inventar: Maschine.py\n\n")
        datei_objekt.write("Dieses Dokument wurde vollautomatisch generiert.\n\n")
        datei_objekt.write("| Quellcode-Datei | Funktion / Terminal-Überschrift |\n")
        datei_objekt.write("| :--- | :--- |\n")
        
        for datei_name in relevante_dateien:
            beschreibung = "Keine Beschreibung extrahierbar."
            try:
                with open(datei_name, "r", encoding="utf-8") as f:
                    # Wir scannen die ersten 15 Zeilen nach einer echten Überschrift
                    for _ in range(15):
                        zeile = f.readline()
                        if not zeile:
                            break
                        zeile = zeile.strip()
                        
                        # Wenn wir dein print("--- ... ---") finden, extrahieren wir den Inhalt!
                        if 'print("---' in zeile or "print('---" in zeile:
                            # Bereinigt den String von print-Klammern und Strichen
                            inhalt = zeile.replace('print("', '').replace('")', '')
                            inhalt = inhalt.replace("print('", "").replace("')", "")
                            beschreibung = inhalt.replace("---", "").strip()
                            break
                        # Alternative: Wir nutzen einen klassischen Kopf-Kommentar, falls kein Print da ist
                        elif zeile.startswith("#") and not zeile.startswith("#!") and "=================" not in zeile:
                            beschreibung = zeile.lstrip("# ").strip()
                            break
            except Exception:
                beschreibung = "🚨 Fehler beim Einlesen der Datei."
                
            datei_objekt.write(f"| `{datei_name}` | {beschreibung} |\n")
            
    print(f"💎 SUCCESS: Das intelligente Inventar '{inventar_datei}' wurde generiert!")

except Exception as fehler:
    print(f"🚨 FEHLER BEIM GENERIEREN DES INVENTARS: {fehler}")

print("\n" + LINIE)
print("⚙️ Inventar-Modul abgeschlossen.")
print(LINIE)