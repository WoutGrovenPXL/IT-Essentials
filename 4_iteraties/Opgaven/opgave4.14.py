som = 0
i = 1
AANTAL_STUDENTEN = 28

while i <= AANTAL_STUDENTEN:
    leeftijd = int(input(f"Geef leeftijd van de student {i}: "))
    som += leeftijd
    i += 1

print("De gemiddelde leeftijd van de studenten = ", som / i)
