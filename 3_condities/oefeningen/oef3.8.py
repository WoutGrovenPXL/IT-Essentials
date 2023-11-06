afstand_vlucht = int(input("Geef de afstand van de vlucht in (in km): "))
klasse_vlucht = int(input("Geef de klasse van de vlucht in (1=toeristenklasse;2=charter;3=zakenreis): "))

totaal_prijs = 0

if afstand_vlucht < 1000:
    totaal_prijs = afstand_vlucht * 0.25
elif (afstand_vlucht >= 1000) and (afstand_vlucht <= 2999):
    totaal_prijs = afstand_vlucht * 0.20
else:
    totaal_prijs = afstand_vlucht * 0.12

if klasse_vlucht == 2:
    totaal_prijs -= (totaal_prijs * 0.20)
elif klasse_vlucht == 3:
    totaal_prijs += (totaal_prijs * 0.30)

print("De prijs van jouw ticket is ", totaal_prijs, " Euro")