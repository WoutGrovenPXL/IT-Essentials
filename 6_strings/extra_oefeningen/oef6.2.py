from random import randint


def genereer_tekst(aantal_tekens):
    genereerde_tekst = ""
    random_getal = randint(65, 90)

    for i in range(aantal_tekens):
        genereerde_tekst += chr(random_getal)
        random_getal = randint(65, 90)

    return genereerde_tekst


def main():
    aantal_tekens = int(input("Uit hoeveel tekens moet de tekst bestaan: "))
    print(genereer_tekst(aantal_tekens))

if __name__ == "__main__":
    main()
