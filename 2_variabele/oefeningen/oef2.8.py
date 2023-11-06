afgelegde_km = float(input("Geef het aantal afgelegde km per jaar: "))
verbruik = float(input("Geef het verbruik in liter per 100 km in: "))
prijs_per_liter = float(input("Geef de prijs per liter in: "))

totale_prijs = ((afgelegde_km / 100) * verbruik) * prijs_per_liter
print("De totale kosten per jaar voor het opgegeven aantal km is: ", totale_prijs)

prijs_per_km = (verbruik / 100) * prijs_per_liter
print("De kostprijs per km rijden is: ", prijs_per_km)