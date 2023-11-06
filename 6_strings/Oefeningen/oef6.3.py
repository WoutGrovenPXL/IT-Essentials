def main():
    aantal_karakters = int(input("Hoeveel karakters wil u ingeven? "))
    positieve_getallen = 0

    for i in range(aantal_karakters):
        karakter = input("Geef een karakter: ")

        if karakter.isalpha():
            if karakter.isupper():
                print(f"{karakter} is een hoofdletter")
            else:
                print(f"{karakter} is een kleineletter")
        elif karakter.isdigit() and int(karakter) > 0:
            positieve_getallen += int(karakter)
        else:
            print(f"{karakter} is onbekend")

    print(f"Totaal cijfers: {positieve_getallen}")


if __name__ == "__main__":
    main()
