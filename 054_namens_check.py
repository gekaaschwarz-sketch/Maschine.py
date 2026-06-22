def hole_sauberen_namen():
    while True:
        # Deine neues Qualitäts-Format
        name = input("Bitte Name der Fahrer*in eingeben: ")

        # .isalpha() prüft auf Buchstaben (A-Z)
        if name.isalpha():
            return name
        else:
            print("❌️ Fehler: Der Name darf nur aus Buchstaben bestehen!")

# Start
print("--- SYSTEM-CHECK: NAMENS-VALIDIERUNG ---")
name_geprueft = hole_sauberen_namen()
print("✅️ Erfolg: " + name_geprueft + " ist in System.")
