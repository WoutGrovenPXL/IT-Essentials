def bepaal_sterrenbeeld(geboortedatum):
    sterren_beelden = ["Ram", "Stier", "Tweelingen", "Kreeft", "Leeuw", "Maagd", "Weegschaal", "Schorpioen",
                       "Boogschutter", "Steenbok", "Waterman", "Vissen"]

    gesplitse_datum = geboortedatum.split("/")
    dag = gesplitse_datum[0]
    maand = gesplitse_datum[1]

    if (dag <= "21" and maand == "03") or (dag > "21" and maand == "04"):
        return sterren_beelden[0]
    if (dag <= "21" and maand == "04") or (dag > "21" and maand == "05"):
        return sterren_beelden[1]
    if (dag <= "21" and maand == "05") or (dag > "21" and maand == "06"):
        return sterren_beelden[2]
    if (dag <= "21" and maand == "06") or (dag > "21" and maand == "07"):
        return sterren_beelden[3]
    if (dag <= "21" and maand == "07") or (dag > "21" and maand == "08"):
        return sterren_beelden[4]
    if (dag <= "21" and maand == "08") or (dag > "21" and maand == "09"):
        return sterren_beelden[5]
    if (dag <= "21" and maand == "09") or (dag > "21" and maand == "10"):
        return sterren_beelden[6]
    if (dag <= "21" and maand == "10") or (dag > "21" and maand == "11"):
        return sterren_beelden[7]
    if (dag <= "21" and maand == "11") or (dag > "21" and maand == "12"):
        return sterren_beelden[8]
    if (dag <= "21" and maand == "12") or (dag > "21" and maand == "01"):
        return sterren_beelden[9]
    if (dag <= "21" and maand == "01") or (dag > "21" and maand == "02"):
        return sterren_beelden[10]
    if (dag <= "21" and maand == "02") or (dag > "21" and maand == "03"):
        return sterren_beelden[11]


def print_naam(naam, voornaam, geboortedatum):
    string = ""
    string += voornaam[0].upper()
    string += ". "
    string += naam.upper()
    string += " "
    string += bepaal_sterrenbeeld(geboortedatum)

    return string


def main():
    naam = input("Geef de naam van een persoon in / om te eindigen: ")

    while not (naam == "/"):
        voornaam = input("Geef de voornaam: ")
        geboortedatum = input("Geef geboortedatum (dd/mm/yyyy): ")

        print(print_naam(naam, voornaam, geboortedatum))

        naam = input("Geef de naam van een persoon in / om te eindigen: ")


if __name__ == "__main__":
    main()
