def prijs_per_persoon(aantal_sterren, hotel_code):
    totaal_prijs = 0

    begin_hotel_code = hotel_code[:2]

    if begin_hotel_code == "HI":
        totaal_prijs = 70
    else:
        if aantal_sterren == 4 or aantal_sterren == 5:
            totaal_prijs = 60
        elif aantal_sterren == 3:
            if begin_hotel_code == "BR" or begin_hotel_code == "AN":
                totaal_prijs = 60
            else:
                totaal_prijs = 56
        else:
            totaal_prijs = 48

    return totaal_prijs


def prijs_per_kind(aantal_sterren, kindercode, hotel_code):
    totaal_prijs = 0

    begin_hotel_code = hotel_code[:2]

    if kindercode == "A":
        if (aantal_sterren == 1 or aantal_sterren == 2) or (begin_hotel_code != "BR"):
            totaal_prijs = 0
    else:
        totaal_prijs = prijs_per_persoon(aantal_sterren, hotel_code) * 0.5

    return totaal_prijs


def main():
    aantal_volwassenen = int(input("Geef het aantal volwassenen: "))
    aantal_kinderen = int(input("Geef het aantal kinderen: "))
    hotel_code = input("Geef een hotelcode: ")
    eind_string = ""

    while not (hotel_code == "/"):
        aantal_sterren = int(input("Geef het aantal sterren: "))
        kindercode = input("Geef een kindercode: ")

        for i in range(aantal_sterren):
            hotel_code += "*"

        prijs_volwassenen = prijs_per_persoon(aantal_sterren, hotel_code)
        prijs_kind = prijs_per_kind(aantal_sterren, kindercode, hotel_code)
        totaal_prijs = (aantal_volwassenen * prijs_volwassenen) + (aantal_kinderen * prijs_kind)

        eind_string += f"{hotel_code}\t {prijs_volwassenen} {prijs_kind} {totaal_prijs}\n"

        hotel_code = input("Geef een hotelcode: ")

    print(eind_string)


if __name__ == "__main__":
    main()
