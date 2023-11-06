def main():
    alfabet = ""
    for letter in range(ord('a'), ord('z') + 1):
        alfabet += chr(letter)

    print("Alfabet zonder wijzigingen:")
    print(alfabet)

    alfabet_met_hoofdletters = ""
    for i, letter in enumerate(alfabet):
        if i % 2 == 1:
            letter = letter.upper()
        alfabet_met_hoofdletters += letter

    print("\nAlfabet met elke tweede letter in hoofdletters:")
    print(alfabet_met_hoofdletters)

    alfabet_met_x = alfabet_met_hoofdletters.replace('H', 'X')

    print("\nAlfabet met 'H' vervangen door 'X':")
    print(alfabet_met_x)


if __name__ == "__main__":
    main()
