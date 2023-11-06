def main():
    print("1: An Janssen")
    print("2: Bart Vreinds")
    print("3: Andries Michels")
    print("4: Inge kaas")
    keuze = int(input("Maak uw keuze: "))

    stemmen = []

    while not (keuze == 0):
        print("1: An Janssen")
        print("2: Bart Vreinds")
        print("3: Andries Michels")
        print("4: Inge kaas")

        stemmen.append(keuze)

        keuze = int(input("Maak uw keuze: "))

    print(f"An Janssen : {stemmen.count(1)} = {round(stemmen.count(1) * 100 / len(stemmen))}")
    print(f"Bart Vriends : {stemmen.count(2)} = {round(stemmen.count(2) * 100 / len(stemmen))}")
    print(f"Andries Michels : {stemmen.count(3)} = {round(stemmen.count(3) * 100 / len(stemmen))}")
    print(f"Inge Kaas : {stemmen.count(4)} = {round(stemmen.count(4) * 100 / len(stemmen))}")

if __name__ == "__main__":
    main()
