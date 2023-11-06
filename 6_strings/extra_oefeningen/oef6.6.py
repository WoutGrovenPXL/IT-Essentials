def klinker_vervanger(zin, teken):
    nieuwe_zin = ""
    for letter in zin:
        if letter == "a" or letter == "o" or letter == "e" or letter == "i" or letter == "I" or letter == "u":
            nieuwe_zin += teken
        else:
            nieuwe_zin += letter

    return nieuwe_zin


def main():
    zin = input("Geef een zin in: ")
    teken = input("Geef teken in: ")

    print(klinker_vervanger(zin, teken))


if __name__ == "__main__":
    main()
