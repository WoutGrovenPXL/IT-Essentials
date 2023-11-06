hoogte = int(input("Geef de hoogte van de driehoek in: "))

patroon = ""

for column in range(hoogte, 0, -1):
    for rows in range(column):
        patroon += "@ "
    patroon += "\n"

print(patroon)