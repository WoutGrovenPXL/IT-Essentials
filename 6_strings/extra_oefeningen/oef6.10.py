def priortiteit_nummer(naam, naam_partner, inkomen, inkomen_partner, aantal_kinderen, code, teller):
    JAAR = 2023
    gezins_inkomen = inkomen + inkomen_partner
    prioriteit = 0
    socialewoning_jaar = code[-4:]

    if socialewoning_jaar == "N":
        socialewoning_jaar = JAAR - 6

    aantal_jaar_socialewoning = JAAR - int(socialewoning_jaar)

    if aantal_jaar_socialewoning < 5:
        prioriteit = 5
    elif (gezins_inkomen < 2000) and (aantal_kinderen >= 3):
        prioriteit = 1
    elif (gezins_inkomen < 2000) and (aantal_kinderen < 3):
        prioriteit = 2
    elif (gezins_inkomen >= 2000 and gezins_inkomen < 2500):
        prioriteit = 3
    elif (gezins_inkomen >= 2500):
        prioriteit = 4

    string = ""

    if naam == "xx":
        eerste_letter_voornaam_partner = naam_partner.split(" ")[1]
        achternaam_partner = naam_partner.split(" ")[0]

        string += f"{teller}.\tMevrouw {eerste_letter_voornaam_partner[:1]}. {achternaam_partner}\t\t\t\t\t\t{sterren_prioriteit(prioriteit)}\t\t\t{goedkopere_bouwlening(naam_partner, naam, inkomen, inkomen_partner, aantal_kinderen)}\n"
    elif naam_partner == "xx":
        eerste_letter_voornaam = naam.split(" ")[1]
        achternaam = naam.split(" ")[0]

        string += f"{teller}.\tMeneer {eerste_letter_voornaam[:1]}. {achternaam}\t\t\t{sterren_prioriteit(prioriteit)}\t\t\t\t\t\t{goedkopere_bouwlening(naam_partner, naam, inkomen, inkomen_partner, aantal_kinderen)}\n"
    else:
        eerste_letter_voornaam = naam.split(" ")[1]
        achternaam = naam.split(" ")[0]
        achternaam_partner = naam_partner.split(" ")[0]
        string += f"{teller}.\tDe Heer en Mevrouw  {eerste_letter_voornaam[:1]}. {achternaam}-{achternaam_partner}\t\t{sterren_prioriteit(prioriteit)}\t\t\t{goedkopere_bouwlening(naam_partner, naam, inkomen, inkomen_partner, aantal_kinderen)}\n"

    return string


def sterren_prioriteit(prioriteit):
    sterren_prioriteit = ""
    for i in range(prioriteit):
        sterren_prioriteit += "*"
    return sterren_prioriteit


def goedkopere_bouwlening(naam_partner, naam, inkomen, inkomen_partner, aantal_kinderen):
    gezins_inkomen = inkomen + inkomen_partner
    bouwlening = ""

    if naam == "xx" or naam_partner == "xx":
        if (gezins_inkomen < 1500) or (aantal_kinderen >= 1):
            bouwlening = "J"

    return bouwlening


def main():
    lijst = "nr\tfamilienaam\t\t\t\t\t\t\t\t\tprioriteit\tbouwlening\n"
    teller = 0

    code = input("Geef code: ")

    while not (code == "S"):
        naam = input("Geef naam (achternaam voornaam): ")
        naam_partner = input("Geef naam partner (achternaam voornaam): ")
        inkomen = int(input("Geef inkomen: "))
        inkomen_partner = int(input("Geef inkomen partner: "))
        aantal_kinderen = int(input("Geef aantal kinderen: "))
        teller += 1

        lijst += priortiteit_nummer(naam, naam_partner, inkomen, inkomen_partner, aantal_kinderen, code, teller)

        code = input("Geef code: ")

    print(lijst)

if __name__ == "__main__":
    main()
