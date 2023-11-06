from random import randint


def kies_willekeurig_gerecht(gerechten):
    gekozen_gerechten = []

    for i in range(5):
        random_index = randint(0, len(gerechten) - 1)
        gekozen_gerecht = gerechten[random_index]
        gekozen_gerechten.append(gekozen_gerecht)
        gerechten.pop(random_index)

    return gekozen_gerechten


def bepaal_label(gerecht):
    if "veg" in gerecht:
        return f"--> groen label"

    basis_score = 1000

    for letter in gerecht:
        basis_score -= 3
        if letter in "friet":
            basis_score += 100

    ascii_eerste_letter_hoofdletter = ord(gerecht[0].upper()) * 3
    ascii_laaste_letter_kleineletter = ord(gerecht[-1].lower()) * 2

    if ascii_eerste_letter_hoofdletter > ascii_laaste_letter_kleineletter:
        basis_score += 300

    basis_score /= 100
    if basis_score < 10:
        return f"--> orangje label (score = {round(basis_score, 1)})"
    elif basis_score > 10:
        return f"--> rood label (score = {round(basis_score, 1)})"


def main():
    gerechten = ["videe", "goulash", "vegetarische pasta", "pizza", "steak-friet", "tajine(veg)", "penne al forno",
                 "burger", "moussaka"]

    gekozen_gerechten = kies_willekeurig_gerecht(gerechten)
    print(gekozen_gerechten)

    for i in range(5):
        print(f"dag {i + 1} {gekozen_gerechten[i]} {bepaal_label(gekozen_gerechten[i])}")


if __name__ == "__main__":
    main()
