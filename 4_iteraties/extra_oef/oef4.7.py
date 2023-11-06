lengte = int(input("Geef de lengte van de rechthoek: "))
hoogte = int(input("Geef de breedte van de rechthoek: "))

for column in range(hoogte):
    for rows in range(lengte):
        if column == 0 or column == hoogte - 1 or rows == 0 or rows == lengte - 1:
            print("*", end="\t")
        else:
            print(" ", end="\t")
    print(" ")