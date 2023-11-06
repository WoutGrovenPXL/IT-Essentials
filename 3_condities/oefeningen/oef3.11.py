aantal_sterren = int(input("Geef het aantal sterren in (1 - 5): "))
code = input("Geef de code in (O=enkel ontbijt; H=half-pension; V=vol pension; A=all-incl): ")
aantal_overnachtingen = int(input("Geef het aantal overnachtingen in: "))
seizoen = input("Geef het seizoen in (H=hoogseizoen; L=laagseizoen; T=tussenseizoen): ")

prijs_verblijf = 0
prijs_maaltijden = 0
totaal_prijs = 0

if aantal_sterren == 1:
    prijs_verblijf = aantal_overnachtingen * 30
elif (aantal_sterren == 2) or (aantal_sterren == 3):
    prijs_verblijf = aantal_overnachtingen * 40
else:
    prijs_verblijf = aantal_overnachtingen * 55


if code == "O":
    prijs_maaltijden = prijs_verblijf * 0.20
elif code == "H":
    prijs_maaltijden = prijs_verblijf * 0.50
elif code == "V":
    prijs_maaltijden = prijs_verblijf * 0.60
elif code == "A":
    prijs_maaltijden = (prijs_verblijf * 0.60) + (80 * aantal_overnachtingen)

totaal_prijs = prijs_verblijf + prijs_maaltijden

if (seizoen == "L") and ((code == "O") or (code == "H")):
    totaal_prijs -= totaal_prijs * 0.10

print("De prijs voor de vakantie van deze persoon is: ", totaal_prijs)