def main():
    tekst1 = input("tekst1 = ")
    tekst2 = input("tekst2 = ")
    tekst_samen = ""

    if len(tekst1) < 4:
        for i in range(4 - len(tekst1)):
            tekst1 += "*"

    if len(tekst2) < 4:
        tmp = tekst2
        tekst2 = ""
        for i in range(4 - len(tmp)):
            tekst2 += "+"
        tekst2 += tmp

    tekst_samen = tekst1.upper() + tekst2.lower()

    print(f"ouput: {tekst_samen}")


if __name__ == "__main__":
    main()
