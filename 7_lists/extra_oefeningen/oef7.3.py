def main():
    row = []
    column = []

    for i in range(7):
        print(f"Geef de waarden voor kolom {i + 1}")
        for j in range(7):
            waarde = int(input(f"Geef de waarde voor rij {j + 1}: "))
            column.append(waarde)
        row.append(column)
        column = []

    for rij in range(7):
        for kolumn in range(7):
            print(f"\t{row[kolumn][rij]}", end="")
        print()

    sum = 0
    index = 0
    for k in range(len(row)):
        sum += row[k][index]
        index += 1

    print(f"Spoor: {sum}")

if __name__ == "__main__":
    main()