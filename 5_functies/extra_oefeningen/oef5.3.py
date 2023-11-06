from random import randint


def perfectGetal(getal):
    som = 0

    for i in range(1, getal):
        if getal % i == 0:
            som += i

    if som == getal:
        return "Perfect"
    else:
        return "Niet perfect"


def genereer_getal():
    random_getal1 = randint(1, 3)
    random_getal2 = randint(1, 3)
    random_getal3 = randint(1, 3)
    random_getal4 = randint(1, 3)

    string = f"{random_getal1}{random_getal2}{random_getal3}{random_getal4}"

    return int(string)


def main():
    random_getal = randint(1, 100)

    getal = int(input("Geef een geheel getal in: "))
    print(f"Is {getal} een perfect getal? {perfectGetal(getal)}")
    print(f"Is {random_getal} een perfect getal? {perfectGetal(random_getal)}")
    print(f"Is {genereer_getal()} een perfect getal? {perfectGetal(genereer_getal())}")


if __name__ == "__main__":
    main()
