def main():
    getal = int(input("Geef een getal: "))
    lijst = []

    while not (getal == 0):
        lijst.append(getal)

        if lijst.count(getal) > 1:
            print(lijst.index(getal))
            lijst.remove(getal)

        getal = int(input("Geef een getal: "))

    for i in lijst:
        print(i)

if __name__ == "__main__":
    main()
