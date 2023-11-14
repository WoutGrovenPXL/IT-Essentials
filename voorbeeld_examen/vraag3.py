def print_lijst_S(lijst):
    print("Lijst van de bij te bestellen producten")
    for artikel in lijst:
        print(f"Product {artikel[0]} te bestellen: {artikel[1]} stuks")

def print_lijst_A(lijst):
    print("Lijst van de actie artikelen")
    for artikel in lijst:
        print(artikel)

def main():
    artikels = ["S-kaftE34-5-100", "S-DVD345-1-124", "A-penD34-125", "S-boekX33-3-256", "A-bal34-145", "S-boekZ34-2-26",
                "A-ballon34-15"]

    lijst_bijbestellen = []
    lijst_actie_artikelen = []

    for artikel in artikels:
        soort_artikel = artikel[0]
        if soort_artikel == "S":
            in_voorraad = int(artikel.split("-")[3])
            per_hoeveelheid_bijbestelt = int(artikel.split("-")[2])
        else:
            in_voorraad = int(artikel.split("-")[2])

        aantal_artikels = int(input(f"Geef het aantal artikels in voorraad van het artikel {artikel}: "))
        while aantal_artikels > in_voorraad and soort_artikel == "A":
            print("Foute ingave! Zoveel artikels kunnen niet in voorraad zijn.")
            aantal_artikels = int(input(f"Opnieuw: Geef het aantal artikels in voorraad van het artikel {artikel}: "))

        if soort_artikel == "S":
            if aantal_artikels < in_voorraad:
                bijtebestellen = in_voorraad - aantal_artikels
                if bijtebestellen % per_hoeveelheid_bijbestelt != 0:
                    bijtebestellen += per_hoeveelheid_bijbestelt
                lijst_bijbestellen.append([artikel, bijtebestellen])
        else:
            if aantal_artikels > 0:
                lijst_actie_artikelen.append(artikel)

    print_lijst_S(lijst_bijbestellen)
    print_lijst_A(lijst_actie_artikelen)


if __name__ == "__main__":
    main()
