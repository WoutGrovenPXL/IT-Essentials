jaar = int(input("Geef jaartal van de film in: "))
rating = int(input("Geef rating van de film in (1 - 5): "))

basis_prijs = 5

if 2023 - jaar < 2:
    basis_prijs += 1

if (rating == 2) or (rating == 3):
    basis_prijs += 1
elif (rating == 4) or (rating == 5):
    basis_prijs += 2

if basis_prijs > 7:
    basis_prijs = 7

print("De prijs van een film is ", basis_prijs)
