def hotel_kosten(aantal_nachten):
    betaalde_nachten = 0

    for i in range(aantal_nachten):
        if i % 3 != 0:
            betaalde_nachten += 1

    return betaalde_nachten * 140.5


def vliegtuig_kosten(stad):
    totaal = 0

    while not (stad == "Barcelona" or stad == "Rome" or stad == "Berlijn" or stad == "Oslo"):
        stad = input("Foutieve input: geef 1 van de selecteerde steden in: ")

    if stad == "Barcelona":
        totaal = 183
    elif stad == "Rome":
        totaal = 220
    elif stad == "Berlijn":
        totaal = 125
    elif stad == "Oslo":
        totaal = 450

    return totaal


def huurauto_kosten(aantal_dagen):
    totaal = aantal_dagen * 40

    if (aantal_dagen > 3) and (aantal_dagen < 7):
        totaal -= 20
    elif aantal_dagen > 7:
        totaal -= 50

    return totaal


def reis_kosten(stad, aantal_dagen):
    vliegtuig_kost = vliegtuig_kosten(stad)
    huurauto = huurauto_kosten(aantal_dagen)
    hotelkost = hotel_kosten(aantal_dagen)

    return vliegtuig_kost + huurauto + hotelkost


def main():
    stad = input("Geef een reisbestemming in (Barcelona, Rome, Berlijn of Oslo): ")
    aantal_dagen = int(input("Geef het aantal dagen dat je in deze stad zal verbijven: "))
    print(f"De kostprijs van deze reis naar Barcelona bedraagt {reis_kosten(stad, aantal_dagen)} euro")


if __name__ == "__main__":
    main()
