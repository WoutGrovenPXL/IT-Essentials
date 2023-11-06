def verschuldigde_belasting(belastbaar_bedrag):
    totaal_belasting = 0

    if belastbaar_bedrag > 25000:
        totaal_belasting = 25000 * 0.384

    if (belastbaar_bedrag) > 25000 and (belastbaar_bedrag < 30000):
        totaal_belasting += (belastbaar_bedrag - 25000) * 0.5

    if belastbaar_bedrag > 30000:
        totaal_belasting += (belastbaar_bedrag - 25000 - 30000) * 0.6

    return totaal_belasting


def main():
    belastbaar_bedrag = float(input("Geef een belastbaar bedrag in: "))
    print(f"Totaal belastingen die u moet betalen is {verschuldigde_belasting(belastbaar_bedrag)}")


if __name__ == '__main__':
    main()
