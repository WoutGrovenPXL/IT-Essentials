def controle_hoogte(hoogte_poort):
    while not (hoogte_poort >= 2 and hoogte_poort <= 6.5):
        hoogte_poort = int(input("Geef de hoogte van de poort: "))
    return hoogte_poort


def controle_breedte(breedte_poort):
    while not (breedte_poort >= 2 and breedte_poort <= 8):
        breedte_poort = int(input("Geef de breedte van de poort: "))
    return breedte_poort


def bereken_oppervlakte(hoogte_poort, breedte_poort):
    return hoogte_poort * breedte_poort


def bereken_gewicht(hoogte_poort, breedte_poort):
    oppervlakte = bereken_oppervlakte(hoogte_poort, breedte_poort)
    return oppervlakte * 11


def motor_prijs(motor_naam):
    prijs = 0
    if motor_naam == "A101":
        prijs = 120
    elif motor_naam == "A105":
        prijs = 220.5
    elif motor_naam == "X300":
        prijs = 250.5
    return prijs


def bereken_prijs_poort(oppervlakte, prijs_motor, kleur):
    prijs = 0
    if kleur is True:
        prijs = oppervlakte * 113.5 + prijs_motor
        prijs += (oppervlakte * 113.5) * 0.1
    else:
        prijs = oppervlakte * 113.5 + prijs_motor
    return round(prijs)


def genereer_offertenummer(naam_verkoper, prijs_poort):
    prijs_poort_omgekeerd = str(prijs_poort)[::-1]
    return f"2023_{naam_verkoper.upper()}_{prijs_poort_omgekeerd}"


def main():
    naam_verkoper = input("Geef de naam van de verkoper: ")

    hoogte_poort = int(input("Geef de hoogte van de poort: "))
    hoogte_poort = controle_hoogte(hoogte_poort)

    breedte_poort = int(input("Geef de breedte van de poort: "))
    breedte_poort = controle_breedte(breedte_poort)

    oppvlakte_poort = bereken_oppervlakte(hoogte_poort, breedte_poort)
    gewicht_poort = bereken_gewicht(hoogte_poort, breedte_poort)

    kleur = input("Wilt u een speciale kleur? (j/n) ")
    if kleur == "j":
        kleur = True
    else:
        kleur = False

    if gewicht_poort < 150:
        motor_naam = "A101"
    elif gewicht_poort >= 150 and gewicht_poort <= 300:
        motor_naam = "A105"
    else:
        motor_naam = "X300"

    prijs_motor = motor_prijs(motor_naam)
    prijs_poort = bereken_prijs_poort(oppvlakte_poort, prijs_motor, kleur)
    print(genereer_offertenummer(naam_verkoper, prijs_poort))


if __name__ == "__main__":
    main()
