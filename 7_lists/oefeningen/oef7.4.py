def main():
    tekst = "abc Abc 123 z"

    letter_frequencies = []

    for char in tekst:
        if char.isalpha():
            char = char.lower()
            found = False
            for entry in letter_frequencies:
                if entry[0] == char:
                    entry[1] += 1
                    found = True
            if not found:
                letter_frequencies.append([char, 1])

    for entry in letter_frequencies:
        print(f"{entry[0]}: {entry[1]} keer")


if __name__ == "__main__":
    main()
