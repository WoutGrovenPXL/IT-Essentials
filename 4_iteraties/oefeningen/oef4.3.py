getal = int(input("Geef een geheel getal in: "))
som = 0
negatieve_getallen = 0

while not (getal == 0):
    som += getal
    if getal < 0:
        negatieve_getallen += 1

    getal = int(input("Geef een geheel getal in: "))

print(f"De som van de ingegeven getallen is {som}")
print(f"Het aantal negatieve ingegeven getallen is {negatieve_getallen}")