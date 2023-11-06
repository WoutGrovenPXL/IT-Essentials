leeftijd = int(input("Geef jouw leeftijd in: "))

lidgeld = 25

if leeftijd < 12:
    lidgeld = 6
elif (leeftijd >= 12) and (leeftijd < 18):
    lidgeld = 12.5

print("Het lidgeld voor deze persoon van ", leeftijd, " is: ", lidgeld)