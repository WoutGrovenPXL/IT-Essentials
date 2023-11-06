def controleer(lidnummer):
    laaste_twee_cijfers = int(lidnummer % 100)
    tweede_cijfer = int(lidnummer / 100000) % 10
    vierde_cijfer = int(lidnummer / 1000) % 10

    tweede_en_vierde = f"{tweede_cijfer}{vierde_cijfer}"
    if str(laaste_twee_cijfers) == tweede_en_vierde:
        return "Gratis"
    else:
        return "Niet gratis"


def main():
    lidnummer = int(input("Geef een nummer bestaande uit 7 cijfers in: "))
    print(controleer(lidnummer))


if __name__ == "__main__":
    main()
