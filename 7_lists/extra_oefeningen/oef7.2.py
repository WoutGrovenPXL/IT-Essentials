def main():
    nederlandse_woorden = ["nul", "een", "twee", "drie", "vier", "vijf", "zes", "zeven", "acht", "negen"]

    getal = input("Geef een geheel getal: ")

    nederlands_getal = ""
    for cijfer in getal:
        cijfer_woord = nederlandse_woorden[int(cijfer)]
        nederlands_getal += cijfer_woord + " "

    print(nederlands_getal)


if __name__ == "__main__":
    main()
