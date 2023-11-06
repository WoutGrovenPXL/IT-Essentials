inschrijvings_nummer = int(input("Geef nummer van de renner in: "))
eerste_tijd_seconden = int(input("Geef tijd in seconden van deze renner in: "))

renners_langer_dan_uur = 0

if eerste_tijd_seconden > 3600:
    renners_langer_dan_uur += 1

aantal_renners = 1
snelste_renner = eerste_tijd_seconden
nummer_snelste_renner = inschrijvings_nummer

inschrijvings_nummer = int(input("Geef nummer van de renner in: "))

while not (inschrijvings_nummer < 0):

    tijd_seconden = int(input("Geef tijd in seconden van deze renner in: "))

    if tijd_seconden > 3600:
        renners_langer_dan_uur += 1

    if snelste_renner > tijd_seconden:
        snelste_renner = tijd_seconden
        nummer_snelste_renner = inschrijvings_nummer

    aantal_renners += 1

    inschrijvings_nummer = int(input("Geef nummer van de renner in: "))

print(f"Het percentage renners dat er langer dan een uur over doet is {renners_langer_dan_uur * 100 / aantal_renners}")
print(f"De snelste renner is de renner met inschrijfnummer {nummer_snelste_renner}")
print(f"{snelste_renner // 3600} u {snelste_renner // 60} min {snelste_renner % 60} sec")
