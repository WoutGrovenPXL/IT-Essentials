def aanwezigheidsduur(in_uur, in_min, uit_uur, uit_min):
    totaal_in_minuten = (in_uur * 60) + in_min
    totaal_uit_minuten = (uit_uur * 60) + uit_min

    totaal_aanwezigheid = totaal_uit_minuten - totaal_in_minuten

    return totaal_aanwezigheid


def gemiddelde_omzetten_naar_uur_minuten(gemiddelde_duur):
    gemiddelde_uur = gemiddelde_duur // 60
    gemiddelde_minuten = gemiddelde_duur % 60

    return gemiddelde_uur, gemiddelde_minuten


def main():
    aantal_meer_dan_uur = 0
    aantal_bezoekers = 0
    som_aanwezigheid = 0
    in_uur = int(input("Geef het uur van binnen komen: "))

    while not in_uur == 0:
        in_min = int(input("Geef de minuten van binnen komen: "))
        uit_uur = int(input("Geef het van uur van weggaan: "))
        uit_min = int(input("Geef de minuten van weggaan: "))

        aanwezigheids_duur = aanwezigheidsduur(in_uur, in_min, uit_uur, uit_min)

        som_aanwezigheid += aanwezigheids_duur

        if aanwezigheids_duur > 60:
            aantal_meer_dan_uur += 1

        aantal_bezoekers += 1

        in_uur = int(input("Geef het uur van binnen komen: "))

    print(f"Er waren {aantal_meer_dan_uur} meer dan 1 uur binnen")

    gemiddelde_duur = som_aanwezigheid / aantal_bezoekers
    gemiddelde_uur = gemiddelde_omzetten_naar_uur_minuten(gemiddelde_duur)[0]
    gemiddelde_minuten = gemiddelde_omzetten_naar_uur_minuten(gemiddelde_duur)[1]

    print(f"Gemiddelde duur binnen = {gemiddelde_uur} u {gemiddelde_minuten} min")


if __name__ == "__main__":
    main()
