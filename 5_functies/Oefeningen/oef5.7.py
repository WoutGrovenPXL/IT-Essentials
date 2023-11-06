def boete_berekenen(aantal_boeken, aantal_dagen):
    totaal_boete = 0.07 * (aantal_boeken * aantal_dagen)

    if aantal_dagen > 45:
        totaal_boete += 0.84

    return totaal_boete


def main():
    aantal_aanmaningsbrieven = 0

    naam = input("Geef de naam in: ")

    while not naam == "xx":
        aantal_boeken = int(input("Geef het aantal boeken in: "))
        aantal_dagen = int(input("Geef het aantal dagen te laat in: "))

        if aantal_dagen >= 45:
            aantal_aanmaningsbrieven += 1

        print(f"{naam} heeft een boete van {boete_berekenen(aantal_boeken, aantal_dagen)} euro")

        naam = input("Geef de naam in: ")

    print(f"aantal aanmaningsbrieven {aantal_aanmaningsbrieven}")


if __name__ == "__main__":
    main()
