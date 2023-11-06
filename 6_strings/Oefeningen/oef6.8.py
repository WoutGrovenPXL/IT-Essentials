def print_triangle(start_char, num_rows):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    start_index = alphabet.index(start_char)

    for row in range(num_rows):
        for i in range(row + 1):
            current_char = alphabet[(start_index + i) % 26]
            print(current_char, end=" ")
        print()


def main():
    start_char = input("Geef het start-karakter: ").upper()
    num_rows = int(input("Geef het aantal rijen: "))

    print_triangle(start_char, num_rows)


if __name__ == "__main__":
    main()
