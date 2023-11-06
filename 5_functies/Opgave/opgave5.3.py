def printx():
    return "x"


def meerderex(aantal_x):
    string = ""
    for i in range(aantal_x):
        string += printx()
    return string


print(meerderex(15))
