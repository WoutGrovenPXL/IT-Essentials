def main():
    tekst = input("Geef een tekst: ")

    if len(tekst) % 3 == 0:
        print(tekst.upper())
    else:
        print(tekst.lower())


if __name__ == "__main__":
    main()
