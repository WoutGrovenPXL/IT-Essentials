persoonelsnummer = int(input("Geef jouw personeelsnummer in: "))

aantal_mannen = 0
aantal_vrouwen = 0

while not (persoonelsnummer == 0):
    geslacht = int(input("Geef jouw geslacht in (0 = vrouw, 1 = man): "))

    while not (geslacht == 1 or geslacht == 0):
        geslacht = int(input("Foutief geslacht: geef opnieuw in (0 = vrouw, 1 = man): "))

    leeftijd = int(input("Geef jouw leeftijd in: "))
    brutoloon = int(input("Geef jouw brutoloon in: "))

    if geslacht == 1:
        if (leeftijd > 34) or (brutoloon >= 1800):
            aantal_mannen += 1
    else:
        if leeftijd < 25:
            aantal_vrouwen += 1

    persoonelsnummer = int(input("Geef jouw personeelsnummer in: "))

print(f"Het aantal mannen dat aan de voorwaarde voldoet is {aantal_mannen}")
print(f"Het aantal vrouwen dat aan de voorwaarde voldoet is {aantal_vrouwen}")