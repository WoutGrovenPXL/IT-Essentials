def main():

    spreuk = "abracadabra"

    spreuk = spreuk.replace("a", "o")

    print(spreuk)

    count = 0
    for letter in spreuk:
        if letter == 'o':
            count += 1

    print(count)




if __name__ == "__main__":
    main()