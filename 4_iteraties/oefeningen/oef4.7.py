eerste_temperatuur = int(input("Geef temperatuur van dag 1 in: "))
hoogste_temperatuur = eerste_temperatuur

som = eerste_temperatuur

for i in range(2, 11):
    temperatuur = int(input(f"Geef temperatuur van dag {i} in: "))

    som += temperatuur
    if temperatuur > hoogste_temperatuur:
        hoogste_temperatuur = temperatuur


print(f"Het gemiddelde van de temperaturen is {som / i}")
print(f"De hoogste temperatuur is {hoogste_temperatuur}")

