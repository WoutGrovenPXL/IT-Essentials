verbruik_per_kubieke_meter = int(input("Geef het verbruik per m³ in: "))

totaal_prijs = 25

if (verbruik_per_kubieke_meter > 30) and (verbruik_per_kubieke_meter <= 200):
    totaal_prijs += (verbruik_per_kubieke_meter - 30) * 1
elif (verbruik_per_kubieke_meter > 200) and (verbruik_per_kubieke_meter <= 5000):
    totaal_prijs += (verbruik_per_kubieke_meter - 30) * 1.15
elif verbruik_per_kubieke_meter > 5000:
    totaal_prijs += (verbruik_per_kubieke_meter - 30) * 1.175

print("De verbruikskosten van het geleverde water zijn: ", totaal_prijs)

