def tekens(aantal_tekens, symbool):
    string = ""
    for i in range(aantal_tekens):
        string += symbool
        string += " "

    return string

print(tekens(8, "*"))
