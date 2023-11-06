def controle_productcode(productcode):
    eerste_letter = productcode[:1].upper()
    laaste_twee_letter = productcode[-2:]

    if len(productcode) < 8:
        print("Lengte moet 8 zijn")
        return False
    elif not (eerste_letter == "L" or eerste_letter == "R"):
        print("Beginletter is niet oke")
        return False
    elif not (laaste_twee_letter == "bo" or laaste_twee_letter == "no"):
        print("Eindletters zijn niet oke")
        return False
    else:
        print(f"{productcode} is inderdaad een geldige productcode")
        return True


def main():
    productcode = input("Geef een geldige productcode: ")
    while not (controle_productcode(productcode)):
        productcode = input("Geef een geldige productcode: ")


if __name__ == "__main__":
    main()
