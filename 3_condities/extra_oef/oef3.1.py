getal1 = int(input("Geef getal 1 in: "))
getal2 = int(input("Geef getal 2 in: "))
getal3 = int(input("Geef getal 3 in: "))

som = getal1 + getal2

if som < 20:
    som += getal3
else:
    som = "te groot"

print("Resultaat is ", som)