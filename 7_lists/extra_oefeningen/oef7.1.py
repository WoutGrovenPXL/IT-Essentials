def controle_studenten_nummer(invoer):
    studenten_nummers = invoer.split(" ")
    studenten_nummers.pop(0)

    for nummer in studenten_nummers:
        if int(nummer) <= 0:
            nieuw_nummer = input("Geef een nieuw nummer: ")
            studenten_nummers.remove(nummer)
            studenten_nummers.append(nieuw_nummer)


def main():
    invoer = input("Geef invoer: ")
    controle_studenten_nummer(invoer)


if __name__ == "__main__":
    main()
