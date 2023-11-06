def schrikkeljaar_controle(jaar):
    if (jaar % 4 == 0) and (jaar % 100 != 0):
        return True
    elif jaar % 400 == 0:
        return True
    else:
        return False


def main():
    jaar = int(input("Geef het jaar in: "))
    print(f"Is dit een schrikkeljaar? {schrikkeljaar_controle(jaar)}")


if __name__ == "__main__":
    main()
