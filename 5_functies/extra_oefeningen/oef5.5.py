def kinderbijslag(leeftijd, code, hoeveelste_kind):
    totaal_bedrag = 0

    if code == "H":
        totaal_bedrag += 300
    else:
        totaal_bedrag += 75 + (hoeveelste_kind * 70)

    if (leeftijd >= 6) and (leeftijd < 12):
        totaal_bedrag += 25
    elif leeftijd >= 12:
        totaal_bedrag += 50

    return totaal_bedrag


def main():
    som_kinderbijslagen = 0
    aantal_kinderen = int(input("Geef het aantal kinderen in: "))

    for i in range(aantal_kinderen):
        leeftijd = int(input("Geef de leeftijd in: "))
        code = input("Geef de code in: ")
        som_kinderbijslagen += kinderbijslag(leeftijd, code, i)

    print(f"De totale kinderbijslag bedraagt {som_kinderbijslagen}")


if __name__ == "__main__":
    main()
