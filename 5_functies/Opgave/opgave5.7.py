def toon_tafel(tafel):
    for i in range(11):
        print(f"{i} x {tafel} = {i * tafel}")


def main():
    tafel = int(input("Welke tafel wil je zien: "))
    toon_tafel(tafel)

if __name__ == '__main__':
    main()
