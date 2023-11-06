def vervorm(tekst):
    eerste_letters = tekst[0] + tekst[3] + tekst[6]
    tweede_letters = tekst[1] + tekst[4] + tekst[7]
    derde_letters = tekst[2] + tekst[5] + tekst[8]

    return eerste_letters + tweede_letters + derde_letters


def main():
    tekst = input("Geef een tekst in: ")
    print(vervorm(tekst))


if __name__ == "__main__":
    main()
