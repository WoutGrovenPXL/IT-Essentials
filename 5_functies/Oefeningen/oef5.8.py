def kostprijs_berekenen(aantal_vierkante_meter):
    totaal_werk_uren = aantal_personen_voor_kuis(aantal_vierkante_meter)[0]

    return totaal_werk_uren * 12.5


def aantal_personen_voor_kuis(aantal_vierkante_meter):
    aantal_personen = 0

    uren_werk = aantal_vierkante_meter // 160
    werk_1_persoon = (aantal_vierkante_meter % 160) / 160

    totaal_werk = uren_werk + werk_1_persoon

    if totaal_werk > 8:
        aantal_personen = totaal_werk // 8
        werk_1_persoon = totaal_werk % 8

    return totaal_werk, werk_1_persoon, aantal_personen


def main():
    aantal_vierkante_meter = float(input("Geef het aantal m2 dat gekuist moet worden: "))

    while not aantal_vierkante_meter == 0:
        print(f"Het kuisen van deze oppervlakte kost {kostprijs_berekenen(aantal_vierkante_meter)} euro")

        if aantal_personen_voor_kuis(aantal_vierkante_meter)[2] > 0:
            print(f"{aantal_personen_voor_kuis(aantal_vierkante_meter)[2]} personen werken 8 uur")
            print(f"1 persoon werkt {aantal_personen_voor_kuis(aantal_vierkante_meter)[1]}")
        else:
            print(f"1 persoon werkt {aantal_personen_voor_kuis(aantal_vierkante_meter)[0]}")

        aantal_vierkante_meter = float(input("Geef het aantal m2 dat gekuist moet worden: "))


if __name__ == "__main__":
    main()
