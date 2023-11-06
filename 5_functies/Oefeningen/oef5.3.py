def bereken_lidgeld(leeftijd, aantal_kinderen, aansluitings_jaar, inkomen):
    JAAR = 2023
    bedrag = 100

    if leeftijd > 60:
        bedrag -= 15

    if aantal_kinderen > 4:
        bedrag -= 35
    else:
        bedrag -= 7.5 * aantal_kinderen

    if (JAAR - aansluitings_jaar) > 20:
        bedrag -= 12.5

    if inkomen < 7500:
        bedrag -= 25

    if bedrag <= 50:
        bedrag = 50

    return bedrag


def main():
    naam = input("Geef de naam in: ")

    while not (naam == "X" or naam == "x"):
        leeftijd = int(input("Geef de leeftijd in: "))
        aantal_kinderen = int(input("Geef het aantal kinderen in: "))
        inkomen = int(input("Geef het inkomen in: "))
        aansluitings_jaar = int(input("Geef het aansluitingsjaar in: "))

        print(f"Voor {naam} bedraagt het lidgeld {bereken_lidgeld(leeftijd, aantal_kinderen, aansluitings_jaar, inkomen)}")

        naam = input("Geef de naam in: ")


if __name__ == "__main__":
    main()
