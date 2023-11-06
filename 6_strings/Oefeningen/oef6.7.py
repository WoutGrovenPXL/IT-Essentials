from random import randint


def encrypt(tekst):
    encrypted_tekst = ""
    random_getal = randint(2, 24)

    while random_getal % 2 != 0:
        random_getal = randint(2, 24)

    for letter in tekst:
        ascii_letter = ord(letter) + random_getal
        encrypted_tekst += chr(ascii_letter)

    return encrypted_tekst


def main():
    tekst = input("Geef een tekst: ")
    print(encrypt(tekst))


if __name__ == "__main__":
    main()
