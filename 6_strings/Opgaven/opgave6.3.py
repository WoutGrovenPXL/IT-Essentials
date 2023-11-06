def main():
    tekst1 = "Ik ben Wout"
    tekst2 = "iK ben Fout"

    for letter in tekst1:
        for letter_tekst2 in tekst2:
            if (letter == letter_tekst2) and ((letter != " ") or (letter_tekst2 != " ")):
                print(f"{letter} komt op dezelfde plaats als {letter_tekst2}")


if __name__ == "__main__":
    main()
