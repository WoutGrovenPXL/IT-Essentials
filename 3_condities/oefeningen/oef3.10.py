HUIDIG_JAAR = 2023

leeftijd = int(input("Geef jouw leeftijd in: "))
aansluitings_jaar = int(input("Geef jouw aansluitingsjaar bij de club in: "))

basis_bedrag = 100
basis_bedrag -= (HUIDIG_JAAR - aansluitings_jaar) * 2.5

if (leeftijd < 21) or (leeftijd > 60):
    basis_bedrag -= 14.5

if basis_bedrag < 62.5:
    basis_bedrag = 62.5

print("De bijdrage voor dit lid is ", basis_bedrag)

