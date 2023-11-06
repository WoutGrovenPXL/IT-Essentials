def totale_kost_prijs(reanimatie_of_ziekenwagen, afstand_km, lid_mutualiteit):
    totaal_bedrag = 0
    aantal_mutualiteit = 0

    if lid_mutualiteit == "N":
        if reanimatie_of_ziekenwagen == "R":
            totaal_bedrag += 25

            if (afstand_km >= 11) and (afstand_km <= 21):
                totaal_bedrag += (afstand_km - 11) * 2.25
            elif afstand_km <= 21:
                afstand_km -= 11
                totaal_bedrag += (afstand_km - 10) * 2.25
                totaal_bedrag += afstand_km * 1.75
        elif reanimatie_of_ziekenwagen == "Z":
            totaal_bedrag += 20

            if (afstand_km >= 11) and (afstand_km <= 21):
                totaal_bedrag += (afstand_km - 11) * 1.75
            elif afstand_km <= 21:
                afstand_km -= 11
                totaal_bedrag += (afstand_km - 10) * 1.75
                totaal_bedrag += afstand_km * 1.15
    elif lid_mutualiteit == "J":
        aantal_mutualiteit += 1
        if reanimatie_of_ziekenwagen == "R":
            totaal_bedrag += 15

            if afstand_km >= 11:
                totaal_bedrag += (afstand_km - 11) * 1.5
        elif reanimatie_of_ziekenwagen == "Z":
            totaal_bedrag += 10

            if afstand_km >= 11:
                totaal_bedrag += (afstand_km - 11) * 1

    return totaal_bedrag, aantal_mutualiteit


def main():
    totale_kost = 0
    aantal_slachtoffers = 0
    naam = input("Geef een naam in: ")

    while not naam == "/":
        reanimatie_of_ziekenwagen = input("Geef reanimatie- of ziekenwagen R/Z: ")
        afstand_km = int(input("Geef de afstand in km: "))
        lid_mutualiteit = input("Lid mutualiteit J/N: ")

        aantal_slachtoffers += 1

        totale_kost = totale_kost_prijs(reanimatie_of_ziekenwagen, afstand_km, lid_mutualiteit)[0]

        print(f"{naam} totale kostprijs {totale_kost}")

        naam = input("Geef een naam in: ")

    leden_mutualiteit = totale_kost_prijs(reanimatie_of_ziekenwagen, afstand_km, lid_mutualiteit)[1]

    print(f"Het aantal vervoerde slachtoffers {aantal_slachtoffers}")
    print(f"Het percentage dat lid is van de mutualiteit {leden_mutualiteit * 100 / aantal_slachtoffers}")

if __name__ == "__main__":
    main()
