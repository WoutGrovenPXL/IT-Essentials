def get_number_of_tests(geneste_lijst):
    return len(geneste_lijst)


def get_number_of_participants(geneste_lijst):
    return len(geneste_lijst[0])


def get_highest_heart_rate(geneste_lijst):
    hoogste_test = max(geneste_lijst)
    hoogste_hartslag = max(hoogste_test)
    return hoogste_hartslag


def get_lowest_heart_rate(geneste_lijst):
    lowest_test = min(geneste_lijst)
    lowest_heartrate = min(lowest_test)
    return lowest_heartrate


def get_average_heart_rate(geneste_lijst):
    list_average_heart_rate = []
    average = 0
    sum = 0

    for i in range(get_number_of_tests(geneste_lijst)):
        list = geneste_lijst[i]
        for j in range(len(list)):
            sum += list[j]

    return sum


def main():
    resultaten_list = [[72, 75, 71, 73, 72, 76], [91, 90, 94, 93, 88, 81], [130, 135, 139, 142, 129, 138],
                       [120, 118, 110, 105, 121, 119]
                       ]
    for row in range(4):
        print(f"Test {row + 1} ", end="")
        for column in range(6):
            print(f"\t{resultaten_list[row][column]}", end="")
        print()

    print(f"Er zijn {get_number_of_tests(resultaten_list)} testen in de lijst")
    print(f"Er zijn {get_number_of_participants(resultaten_list)} deelnemers in de lijst")
    print(f"{get_highest_heart_rate(resultaten_list)} is de hoogste hartslag")
    print(f"{get_lowest_heart_rate(resultaten_list)} is het laagste hartslag")
    print(f"{get_average_heart_rate(resultaten_list)}")


if __name__ == "__main__":
    main()
