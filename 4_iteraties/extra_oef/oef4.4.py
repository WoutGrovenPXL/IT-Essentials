geslacht = int(input("Geef het geslacht van de werknemer in (1 = vrouw / 2 = man): "))

slechte_conditie = 0
aantal_werknemers = 0

while geslacht == 1 or geslacht == 2:
    afstand_lopen_km = float(input("Geef de afstand in km na 12 min lopen: "))
    afstand_lopen_meter = afstand_lopen_km * 1000

    conditie_getal = (afstand_lopen_meter - 504.9) / 44.73

    if geslacht == 1:
        if conditie_getal < 29:
            slechte_conditie += 1
    elif geslacht == 2:
        if conditie_getal < 36:
            slechte_conditie += 1

    aantal_werknemers += 1

    geslacht = int(input("Geef het geslacht van de werknemer in (1 = vrouw / 2 = man): "))

print(f"Het percentage werknemers met een slechte conditie is {int((slechte_conditie * 100 / aantal_werknemers) / 0.01) / 100}")