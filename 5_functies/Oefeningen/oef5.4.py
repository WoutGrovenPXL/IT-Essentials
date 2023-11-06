from random import randint


def feedback(getal, random_getal):
    if getal == random_getal:
        return True
    elif getal > random_getal:
        return "Lager"
    elif getal < random_getal:
        return "Hoger"


def main():
    random_getal = randint(0, 10)

    kansen = 3

    getal = int(input("Geef een getal in: "))

    while kansen > 0:
        if feedback(getal, random_getal) == "Lager":
            print("Lager")
            kansen -= 1
        elif feedback(getal, random_getal) == "Hoger":
            print("Hoger")
            kansen -= 1
        else:
            print("Proficiat, het getal is geraden")
            break

        getal = int(input("Geef een getal in: "))

    if kansen <= 0:
        print("Je 4 beurten zijn voorbij.")


if __name__ == "__main__":
    main()
