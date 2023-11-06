def tekens(aantal_tekens, symbool):
    string = ""
    for i in range(aantal_tekens):
        string += symbool
        string += " "

    return string


def rechthoek(hoogte, breedte, symbool):
    string = ""
    for i in range(hoogte):
        string += tekens(breedte, symbool)
        string += "\n"
    return string


print(rechthoek(4, 7, "*"))
