def keer_om_n(tekst, n):
    nieuwe_tekst = ""

    for letter in tekst[::-1]:
        for i in range(n):
            nieuwe_tekst += letter

    return nieuwe_tekst


def main():
    print(keer_om_n("cum", 100))


if __name__ == "__main__":
    main()
