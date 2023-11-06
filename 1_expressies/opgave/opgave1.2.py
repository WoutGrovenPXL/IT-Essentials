prijs_boek = 24.95

prijs_boek_met_korting = prijs_boek - prijs_boek * 40 / 100
prijs_eerste_boek = 3 + prijs_boek_met_korting
prijs_andere_boeken = (0.75 + prijs_boek_met_korting) * 59

totaal = prijs_eerste_boek + prijs_andere_boeken
print(totaal)


