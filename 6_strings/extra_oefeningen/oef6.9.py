def vercijfer(tekst):
    i = 0
    groep = ""
    nieuwe_tekst = ""
    for letter in tekst:
        groep += letter
        i += 1
        if i == 5:
            nieuwe_tekst += groep[::-1]
            groep = ""
            i = 0

    return nieuwe_tekst + groep


def main():
    tekst = input("Geef een tekst: ")
    print(vercijfer(tekst))


if __name__ == "__main__":
    main()
