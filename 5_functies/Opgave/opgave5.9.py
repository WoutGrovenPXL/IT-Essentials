from random import randint, random

def main():
    random_getal = randint(0, 10)
    print(random_getal)

    print("\n")

    for i in range(11):
        random_getal = randint(0, 10)
        print(random_getal)

    print("\n")

    random_getal = randint(-200, 1000)

    while random_getal % 10 == 0:
        random_getal = randint(-200, 1000)
        print(random_getal)

    print("\n")

    random_getal = random(0, 100)
    print(random_getal)


if __name__ == "__main__":
    main()
