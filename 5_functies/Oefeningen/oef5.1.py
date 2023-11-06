def omzetting(bedrag, wisselkoers):
    return bedrag * wisselkoers


def main():
    wisselkoers = float(input("Geef wisselkoers in: "))
    bedrag = float(input("Geef het om te zetten bedrag in euro in: "))

    while not bedrag == 0:
        print(f"Bedrag in dollar is {omzetting(bedrag, wisselkoers)}")
        bedrag = float(input("Geef het om te zetten bedrag in euro in: "))

if __name__ == "__main__":
    main()
