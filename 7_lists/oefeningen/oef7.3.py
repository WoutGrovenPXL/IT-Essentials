def main():
    positieve_getallen = []
    negatieve_getallen = []

    for i in range(10):
        getal = int(input(f"Geef een geheel getal {i + 1} in: "))

        if getal >= 0:
            positieve_getallen.append(getal)
        else:
            negatieve_getallen.append(getal)

    print(f"{len(positieve_getallen)} positieve getallen")
    print(positieve_getallen)
    for i in positieve_getallen:
        print(i, end=" ")

    print(f"{len(negatieve_getallen)} negatieve getallen")
    print(negatieve_getallen)
    for i in negatieve_getallen:
        print(i, end=" ")

    kleinte_waarde = negatieve_getallen[0]
    for i in negatieve_getallen:
        if i < kleinte_waarde:
            kleinte_waarde = i

    print(f"Het kleinste getal van de negatieve getallen is {kleinte_waarde}")


if __name__ == "__main__":
    main()
