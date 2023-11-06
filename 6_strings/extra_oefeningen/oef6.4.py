def sorteer(tekst):
    nieuwe_tekst = ""
    gesorteerde_lijst = sorted(tekst)

    for letters in gesorteerde_lijst:
        nieuwe_tekst += letters

    return nieuwe_tekst


def main():
    print(sorteer("abdaba"))


if __name__ == "__main__":
    main()
