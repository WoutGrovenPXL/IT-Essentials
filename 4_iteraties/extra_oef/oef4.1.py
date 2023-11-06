PRIJS_JETON = 0.70

for i in range(1, 51):
    print(f"{i} jetons = {int(i * PRIJS_JETON / 0.01) / 100}")