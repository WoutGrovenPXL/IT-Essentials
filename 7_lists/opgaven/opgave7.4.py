def main():
    lijst = []
    gemiddelde = 0
    som = 0
    for i in range(10):
        getal = int(input("Geef een getal: "))
        lijst.append(getal)
        som += getal

    gemiddelde = som / len(lijst)

    kleiner_dan_gemiddelde = 0
    for i in lijst:
        if i < gemiddelde:
            kleiner_dan_gemiddelde += 1

    print(gemiddelde, kleiner_dan_gemiddelde)


if __name__ == "__main__":
    main()
