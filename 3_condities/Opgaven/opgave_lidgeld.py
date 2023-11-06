burgelijke_staat = int(input("Geef uw burgerlijke staat (1 = ongehuwd, 2 = gehuwd, 3 = weduw(e)(naar)): "))
leeftijd = int(input("Geef uw leeftijd: "))
lidgeld = 0

#a
if burgelijke_staat == 1:
    lidgeld = 25
elif burgelijke_staat == 2:
    lidgeld = 20
elif burgelijke_staat == 3:
    lidgeld = 15

#b
if (burgelijke_staat == 1) and (leeftijd < 30):
    lidgeld = 25
else:
    lidgeld = 15


#c
if (burgelijke_staat == 1) or (leeftijd < 30):
    lidgeld = 25
else:
    lidgeld = 15

#d
if burgelijke_staat == 1:
    lidgeld = 25
elif (burgelijke_staat == 2) and (leeftijd < 30):
    lidgeld = 30
else:
    lidgeld = 15