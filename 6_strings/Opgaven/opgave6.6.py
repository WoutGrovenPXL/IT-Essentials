def main():
    string = input("Geef een string: ")

    if len(string) % 2 == 0:
        lengte_woord = int(len(string) / 2)
        eerste_letter = string[lengte_woord - 1].upper()
        tweede_letter = string[lengte_woord].upper()
        nieuwe_string = string[:lengte_woord - 1] + eerste_letter + tweede_letter + string[lengte_woord + 1:]

    else:
        lengte_woord = int(len(string) / 2)
        letter = string[lengte_woord].upper()
        nieuwe_string = string[:lengte_woord] + letter + string[lengte_woord + 1:]

    print(nieuwe_string)


if __name__ == "__main__":
    main()
