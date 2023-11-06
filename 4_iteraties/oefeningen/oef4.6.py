artikelnummer = int(input("Geef artikelnummer in: "))
eenheidsprijs = int(input("Geef einheidsprijs in: "))
aantal = int(input("Geef aantal in: "))

totaal = 0

while not (artikelnummer == 999):
    totaal += aantal * eenheidsprijs

    print(f"artikel nr = {artikelnummer} / hoeveelheid = {aantal} / eenheidsprijs = {eenheidsprijs} / bedrag = {aantal * eenheidsprijs}")

    artikelnummer = int(input("Geef artikelnummer in: "))
    eenheidsprijs = int(input("Geef einheidsprijs in: "))
    aantal = int(input("Geef aantal in: "))

print(f"Het totale bedrag van de aankoop is {totaal}")