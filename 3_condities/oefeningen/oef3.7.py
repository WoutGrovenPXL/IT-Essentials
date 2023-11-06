resultaat1 = int(input("Geef resultaat 1 in: "))
resultaat2 = int(input("Geef resultaat 2 in: "))
resultaat3 = int(input("Geef resultaat 3 in: "))

behaald_percentage = (resultaat1 + resultaat2 + resultaat3) * 100 / 60
graad = ""

if behaald_percentage < 60:
    graad = "onvoldoende"
elif (behaald_percentage >= 60) and (behaald_percentage < 70):
    graad = "voldoende"
elif (behaald_percentage >= 70) and (behaald_percentage < 80):
    graad = "onderscheiding"
elif (behaald_percentage >= 80) and (behaald_percentage < 90):
    graad = "grote onderscheiding"
else:
    graad = "grootste onderscheiding"

print("Het percentage van deze student is ", behaald_percentage, " en zijn graad is", graad)