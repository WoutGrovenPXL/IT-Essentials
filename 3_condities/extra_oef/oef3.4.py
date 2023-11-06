naam_speler = input("Geef naam van de speler in: ")
prijs_vorig_seizoen = int(input("Geef de prijs van vorig seizoen in: "))
leeftijd = int(input("Geef de leeftijd in: "))
beoordelingscijfer = int(input("Geef beoordelingscijfer in (0 - 10): "))
type_speler = input("Geef type van de speler in (A=Aanvaller; M=Middenvelder; V=verdediger; D=Doelman): ")
aantal_doelpunten = int(input("Geef het aantal doelpunten in: "))

nieuwe_prijs = prijs_vorig_seizoen

if leeftijd < 25:
    nieuwe_prijs += nieuwe_prijs * 0.10
elif leeftijd > 30:
    nieuwe_prijs -= nieuwe_prijs * 0.05

if type_speler == "A":
    if aantal_doelpunten > 5:
        nieuwe_prijs += 50000 + ((aantal_doelpunten - 5) * 20000)
    else:
        nieuwe_prijs += aantal_doelpunten * 10000
elif (type_speler == "M") or (type_speler == "V") or (type_speler == "D"):
    nieuwe_prijs += beoordelingscijfer * 10000
    if type_speler == "D":
        if aantal_doelpunten >= 20:
            nieuwe_prijs -= (aantal_doelpunten - 21) * 9000

print("Naam: ", naam_speler)
print("Prijs vorig seizoen: ", prijs_vorig_seizoen)
print("Prijs nieuw seizoen: ", nieuwe_prijs)
