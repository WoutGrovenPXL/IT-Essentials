from random import randint

def score_bepaling(naam, jaar, bezoeken_frequentie, snack):
    basis_score = 0

    lijst = []

    i = 0
    for letter in naam:
        if letter in "cinema":
            index = naam.find(letter, i) + 1
            ascii_letter = ord(letter)
            lijst.append([index, ascii_letter])
        i += 1

    result = [x * y for x, y in lijst]
    for i in range(len(result)):
        basis_score += result[i]

    basis_score += jaar
    echte_score = basis_score

    if bezoeken_frequentie == 1:
        echte_score /= 2
    elif bezoeken_frequentie == 2:
        echte_score *= 2
    else:
        echte_score *= 3

    if (snack == "N") and (bezoeken_frequentie == 1 or bezoeken_frequentie == 2):
        echte_score -= 1050

    return basis_score, echte_score

def bepaal_prijs():
    string = ""

    getal1 = randint(1, 9)
    getal2 = randint(0, 9)
    getal3 = randint(0, 9)
    getal4 = randint(1, 9)

    som = getal1 + getal2 + getal3 + getal4

    string += str(getal1) + str(getal2) + str(getal3) + str(getal4)

    genereerd_getal = int(string)
    if genereerd_getal < 5000 and genereerd_getal % 2 != 0:
        genereerd_getal += 1
        som += 1

    return som, genereerd_getal


def main():

    score_lijst = []

    naam = input("Geef jouw naam in: ")
    while not (naam == "xxx" or naam == "qqq"):
        jaar = int(input("In welk jaar ben jij geboren?: "))
        bezoeken_frequentie = int(input("Hoe vaak ga je naar kinepolis per maand (1=weinig, 1=matig, 3=veel): "))
        snack = input("Wat eet je bij kinepolis (P=popcorn, C=chips, N=niets): ")

        basisscore = score_bepaling(naam, jaar, bezoeken_frequentie, snack)[0]
        echte_score = score_bepaling(naam, jaar, bezoeken_frequentie, snack)[1]
        score_lijst.append([naam, echte_score])

        print(f"{naam}: basisscore = {basisscore}")

        naam = input("Geef jouw naam in: ")

    hoogste_score = max(score_lijst)
    print(f"{hoogste_score[0]} : Jij hebt gewonnen!")
    print(f"Jouw score is: {hoogste_score[1]}")
    print(f"Het random gegenereerd getal is {bepaal_prijs()[1]}")
    print(f"{hoogste_score[0]}, jij wint hierbij {bepaal_prijs()[0]} filmtickets.")


if __name__ == "__main__":
    main()
