naam = input("Geef de naam van de manager in: ")

aantal_managers = 0
aantal_geslaagd = 0

while not (naam == "xx" or naam == "XX"):
    test1 = int(input("Test1: "))
    test2 = int(input("Test2: "))
    test3 = int(input("Test3: "))

    gemiddelde = (test1 + test2 + test3) / 3
    if gemiddelde < 70:
        resultaat = "faalt"
    else:
        resultaat = "slaagt"
        aantal_geslaagd += 1

    aantal_managers += 1

    print(
        f"{naam} Test1: {test1} Test2: {test2} Test3: {test3} Gemiddelde: {int(gemiddelde / 0.01) / 100} Resultaat: {resultaat}")

    naam = input("Geef de naam van de manager in: ")

print(f"Er slaagde {aantal_geslaagd * 100 / aantal_managers}% van de {aantal_managers} deelnemers")
