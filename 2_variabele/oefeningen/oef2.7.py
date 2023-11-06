lengte = float(input("Geef de lengte van het tapijt in (in meter): "))
breedte = float(input("Geef de breedte van het tapijt in (in meter): "))
prijs = float(input("Geef de prijs per vierkante meter in: "))
plaatsingskosten = float(input("Geef de plaatsingskoster per vierkante meter in: "))

prijs_tapijt = (lengte * breedte) * prijs
print("De kostprijs van het tapijt is: ", prijs_tapijt)
prijs_plaatsing = (lengte * breedte) * plaatsingskosten
print("De plaatsingskosten van het tapijt zijn: ", prijs_plaatsing)
print("De totale kost is: ", prijs_tapijt + prijs_plaatsing)