gewicht = int(input("Geef een gewicht: "))

if gewicht > 20:
    print("Er moet een toeslag van 25 euro betaald worden voor bagage die te zwaar is.")
elif gewicht < 20:
    print("Goede reis!")
else:
    print("Poeh! Dat gewicht is percies goed!")