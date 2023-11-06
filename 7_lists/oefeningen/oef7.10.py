from random import randint

def zet_schepen():
    row_schip1 = randint(0, 2)
    row_schip2 = randint(0, 2)
    row_schip3 = randint(0, 2)

    check_rows(row_schip1, row_schip2)
    check_rows(row_schip1, row_schip3)
    check_rows(row_schip2, row_schip3)

    colummn_schip1 = randint(0, 3)
    colummn_schip2 = randint(0, 3)
    colummn_schip3 = randint(0, 3)

    bord = [[" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "]]

    ship = True
    bord[row_schip1][colummn_schip1] = ship
    bord[row_schip2][colummn_schip2] = ship
    bord[row_schip3][colummn_schip3] = ship

    return bord


def check_rows(row1, row2):
    while row1 == row2:
        row1 = randint(0, 2)
    return row1


def maak_speel_bord(speel_bord):
    column_headers = ["A", "B", "C", "D"]

    for row in range(4):
        print(f"\t{column_headers[row]}", end=" ")

    print()
    for row in range(3):
        print(f"{row + 1} ", end="")
        for column in range(4):
            print(f"\t{speel_bord[row][column]}", end="")
        print()


def schiet(cel, schepen):
    column = cel[0]

    if column == "A":
        column = 0
    elif column == "B":
        column = 1
    elif column == "C":
        column = 2
    elif column == "D":
        column = 3

    row = int(cel[1])
    row -= 1

    indexs_ships = []
    for i in range(len(schepen)):
        for j in range(len(schepen[i])):
            if schepen[i][j] == True:
                indexs_ships.append([i, j])

    return row, column, indexs_ships


def update_speel_bord(cel, speel_bord, schepen):
    row = schiet(cel, schepen)[0]
    column = schiet(cel, schepen)[1]
    indexs_ships = schiet(cel, schepen)[2]

    index_shots = [row, column]
    if index_shots in indexs_ships:
        speel_bord[row][column] = "."
        schepen[row][column] = False
        print("Raak!")
    else:
        speel_bord[row][column] = "X"
        print("Mis!")

    maak_speel_bord(speel_bord)


def check_win(schepen):
    flat_list = [item for sublist in schepen for item in sublist]
    has_true = any(item == True for item in flat_list)
    if not has_true:
        return True


def main():
    speel_bord = [[" ", " ", " ", " "],
                  [" ", " ", " ", " "],
                  [" ", " ", " ", " "]]

    maak_speel_bord(speel_bord)
    schepen = zet_schepen()

    win = False
    teller = 0
    while not (win == True):
        kies_cel = input("Kies een cel: ")
        schiet(kies_cel, schepen)
        update_speel_bord(kies_cel, speel_bord, schepen)
        win = check_win(schepen)
        teller += 1

    print(f"Je gebruike {teller} zetten")


if __name__ == "__main__":
    main()
