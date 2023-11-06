EENHEIDSPRIJS_ARTIKEL = 11.5
BTW = 0.21

aantal_artikels = int(input("Hoeveel stuks wil je? "))

totaal_prijs = (aantal_artikels * EENHEIDSPRIJS_ARTIKEL) + (aantal_artikels * EENHEIDSPRIJS_ARTIKEL * BTW)

if totaal_prijs > 1000:
    totaal_prijs -= (totaal_prijs * 0.10)

print("De totale prijs is ", totaal_prijs)