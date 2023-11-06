def string_vervanger(string):
    nieuwe_string = ""

    for letter in string:
        if (ord(letter) < 97 or ord(letter) > 122):
            nieuwe_string += " "
        else:
            nieuwe_string += letter

    return nieuwe_string


def main():
    string = "ph@tFDFSSQDFDfdfdfsfsfeFDZEfef l00t"
    print(string_vervanger(string))


if __name__ == "__main__":
    main()
