from random import randint


def controleer_output():
    random_getal1 = randint(0, 20)
    random_getal2 = randint(0, 20)

    while random_getal1 < random_getal2:
        random_getal2 = randint(0, 20)

    return random_getal1, random_getal2


def main():
    for i in range(1, 6):
        print(f"reeks {i}")
        for j in range(1, 6):
            random_getal1, random_getal2 = controleer_output()[0], controleer_output()[1]

            print(f"{j}) {random_getal1} - {random_getal2} = ")


if __name__ == "__main__":
    main()
