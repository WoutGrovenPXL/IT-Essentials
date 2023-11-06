PRIJS_VOLWASSEN = 11
PRIJS_ONDER_TWAALF = 6

aantal_volwassenen = int(input("Geef het aantal volwassenen in: "))
aantal_kinderen = int(input("Geef het aantal kinderen in: "))
print("De totale prijs is ", (PRIJS_VOLWASSEN * aantal_volwassenen) + (PRIJS_ONDER_TWAALF * aantal_kinderen))
