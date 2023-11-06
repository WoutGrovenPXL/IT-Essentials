def main():
    string = "diT was eEne ttEkS"

    eerste_t = string.lower().find("t")
    nieuwe_string = ""

    if eerste_t == -1:
        print("De gegeven tekst bevat geen t of T")
    elif len(string) % 2 != 0:
        nieuwe_string = string[:eerste_t + 1] + string[1 + eerste_t:].upper()
        print(nieuwe_string)
    elif len(string) % 2 == 0:
        nieuwe_string = string[:eerste_t + 1] + string[1 + eerste_t:].lower()
        print(nieuwe_string)


if __name__ == "__main__":
    main()
