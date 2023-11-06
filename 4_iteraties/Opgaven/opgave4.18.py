getal = int(input("Geef een getal tussen 0 en 10: "))

while (getal <= 0 or getal >= 10):
    getal = int(input("Geef een getal tussen 0 en 10: "))

print(getal)

#schrijf eerst de stopvoorwaarde: getal > 0 and getal < 10
#inverteer de stopvoorwaarde: not(getal > 0 and getal < 10)
#of werkt uit: getal <= 0 or getal >= 10