lengte = int(input("Geef de lengte van de rechthoek: "))
hoogte = int(input("Geef de breedte van de rechthoek: "))

for column in range(hoogte):
    for rows in range(lengte):
        print("*", end="\t")
    print(" ")