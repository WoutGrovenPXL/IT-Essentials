getal1 = float(input("Geef getal 1 in: "))
getal2 = float(input("Geef getal 2 in: "))

kleinste_getal = getal1
grooste_getal = getal1

if kleinste_getal > getal2:
    kleinste_getal, grooste_getal = getal2, getal1

print("Het kleinste getal is ", kleinste_getal)
print("Het kwadraat van het kleinste getal is ", kleinste_getal ** 2)
print("Het grootste gedeeld door het kleinste is ", grooste_getal / kleinste_getal)


