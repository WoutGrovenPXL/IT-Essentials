BINNEN_BELGIE = 0.12
BUITENLAND = 0.50
VAST_BEDRAG = 20

aantal_belgische_gesprekken = int(input("Geef het aantal Belgische gepsrekken: "))
aantal_minuten_buitenland = int(input("Geef het aantal minuten dat je naar het buitenland telefoneerde: "))

prijs = 20 + (20 * 21 / 100)
prijs += (BINNEN_BELGIE * aantal_belgische_gesprekken) + (BUITENLAND * aantal_minuten_buitenland)

print("Te betalen = ", prijs, " euro")