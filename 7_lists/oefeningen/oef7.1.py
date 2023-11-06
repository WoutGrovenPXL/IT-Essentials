def main():
    list = []
    for i in range(15):
        getal = int(input("Geef een geheel getal: "))
        list.append(getal)

    gemiddelde = sum(list) / len(list)
    aantal_onder_gemiddelde = 0

    for i in list:
        if i < gemiddelde:
            aantal_onder_gemiddelde += 1

    percentage_onder_gemiddelde = (aantal_onder_gemiddelde * 100 / len(list))

    print(f"Gemiddelde: {gemiddelde}")
    print(f"Aantal onder gemiddelde: {aantal_onder_gemiddelde}")
    print(f"Percentage onder gemiddelde: {round(percentage_onder_gemiddelde)}")


if __name__ == "__main__":
    main()
