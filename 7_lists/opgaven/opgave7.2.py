def main():
    lijst = [10, 1, 2, 0, 4, 5]
    kleinste_getal = lijst[0]
    grooste_getal = lijst[1]
    som = 0

    for i in lijst:
        if i < kleinste_getal:
            kleinste_getal = i
        elif i > grooste_getal:
            grooste_getal = i

        som += i

    print(grooste_getal, kleinste_getal, som)


if __name__ == "__main__":
    main()
