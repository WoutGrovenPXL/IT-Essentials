def bepaal_leeftijd(deelnemer_informatie, huidige_datum):
    leeftijd = 0

    verjaardag_deelnemer = deelnemer_informatie.split(" ")[1]

    verjaardag_deelnemer_dag = int(verjaardag_deelnemer.split("/")[0])
    verjaardag_deelnemer_maand = int(verjaardag_deelnemer.split("/")[1])
    verjaardag_deelnemer_jaar = int(verjaardag_deelnemer.split("/")[2])

    huidige_datum_dag = int(huidige_datum.split("/")[0])
    huidige_datum_maand = int(huidige_datum.split("/")[1])
    huidige_datum_jaar = int(huidige_datum.split("/")[2])

    leeftijd = huidige_datum_jaar - verjaardag_deelnemer_jaar

    return leeftijd


def seconden_omzetten(deelnemer_informatie):
    seconden = int(deelnemer_informatie.split(" ")[3])

    uren = seconden // 3600
    resterende_seconden = seconden % 3600
    minuten = resterende_seconden / 60

    if minuten - (resterende_seconden // 60) > 0.3:
        minuten += 1

    return uren, int(minuten)


def resultaat_kandidaat(deelnemer_informatie, correcte_antwoorden):
    beantwoorde_vragen = deelnemer_informatie.split(" ")[2]
    antwoord_lijst = []
    correcte_antwoorden_lijst = []
    punten = 20

    for letter in beantwoorde_vragen:
        antwoord_lijst.append(letter)

    for letter in correcte_antwoorden:
        correcte_antwoorden_lijst.append(letter)

    for i in range(len(antwoord_lijst)):
        if antwoord_lijst[i] == "E":
            punten += 0
        elif antwoord_lijst[i] == correcte_antwoorden_lijst[i]:
            punten += 2
        elif antwoord_lijst[i] != correcte_antwoorden_lijst[i]:
            punten -= 1

    return punten


def main():
    lijst_resultaten = []
    teller = 1

    correcte_antwoorden = input("Geef de correcte antwoorden op de vragen: ")
    huidige_datum = input("Geef de huidige datum (dd/mm/yyyy): ")

    deelnemer_informatie = input("Geef deelnemer informatie: ")

    while not (deelnemer_informatie == "0"):
        leeftijd = bepaal_leeftijd(deelnemer_informatie, huidige_datum)
        uren = seconden_omzetten(deelnemer_informatie)[0]
        minuten = seconden_omzetten(deelnemer_informatie)[1]
        punten = resultaat_kandidaat(deelnemer_informatie, correcte_antwoorden)

        string_resultaat = f"{teller}.\t{deelnemer_informatie.split(' ')[0]}\t{leeftijd} jaar\t{uren}u {minuten}m\t{punten} ptn"
        lijst_resultaten.append(string_resultaat)

        teller += 1
        deelnemer_informatie = input("Geef deelnemer informatie: ")

    for resultaat in lijst_resultaten:
        print(resultaat)


if __name__ == "__main__":
    main()
