from random import randint


def main():
    list = []

    for i in range(500):
        random_getal = randint(0, 10000)
        list.append(random_getal)

    aantal_groter_dan_5000 = []
    aantal_kleiner_dan_5000 = []

    for i in list:
        if i > 5000:
            aantal_groter_dan_5000.append(i)
        else:
            aantal_kleiner_dan_5000.append(i)

    print(f"Groter dan 5000: {len(aantal_groter_dan_5000)}")
    print(f"Kleiner dan 5000: {len(aantal_kleiner_dan_5000)}")

    som = 0

    if len(aantal_groter_dan_5000) < 250:
        print(sum(aantal_groter_dan_5000))
    elif len(aantal_groter_dan_5000) > 250:
        for i in aantal_groter_dan_5000:
            if i > 8000:
                som += i
        print(som)


if __name__ == "__main__":
    main()
