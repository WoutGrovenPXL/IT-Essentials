def gemiddelde_score(resultaten_lijst, vak):
    vak -= 1
    sum = 0
    for i in range(len(resultaten_lijst)):
        sum += resultaten_lijst[i][vak]

    return sum / len(resultaten_lijst)


def laagste_score(resultaten_lijst, vak):
    laagste_score = 20
    student = 0
    vak -= 1

    for i in range(len(resultaten_lijst)):
        if resultaten_lijst[i][vak] < laagste_score:
            laagste_score = resultaten_lijst[i][vak]
            student = i + 1

    return laagste_score, student


def main():
    resultaten_lijst = []
    studenten_lijst = []

    for i in range(5):
        print(f"Geef de punten voor student {i + 1}")
        for j in range(4):
            punt = int(input(f"Vak {j + 1}: "))
            studenten_lijst.append(punt)
        resultaten_lijst.append(studenten_lijst)
        studenten_lijst = []

    for row in range(5):
        print(f"stud{row + 1} ", end="")
        for column in range(4):
            print(f"\t{resultaten_lijst[row][column]}", end="")
        print()

    for i in range(4):
        print(
            f"Vak {i + 1} Gemiddelde score: {gemiddelde_score(resultaten_lijst, i + 1)} Laagste score: {laagste_score(resultaten_lijst, i + 1)[0]} behaald door student: {laagste_score(resultaten_lijst, i + 1)[1]}")


if __name__ == "__main__":
    main()
