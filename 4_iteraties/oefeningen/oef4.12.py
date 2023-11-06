familienaam = input("Geef jouw familienaam in: ")

hoogste_premie = 0
totaal_premie = 0
premie = 0

while not (familienaam == "/" or familienaam == "*"):

    voornaam = input("Geef jouw voornaam in: ")
    dienstjaren = int(input("Geef het aantal dienstjaren in: "))

    while dienstjaren <= 0 or dienstjaren >= 40:
        dienstjaren = int(input("Geef een juist aantal dienstjaren in (tussen 0 en 40)): "))

    if dienstjaren < 5:
        premie = 0
    else:
        premie = dienstjaren * 25

    totaal_premie += premie

    if premie > hoogste_premie:
        hoogste_premie = premie

    print(f"familienaam = {familienaam}")
    print(f"voornaam = {voornaam}")
    print(f"aantal dienstjaren = {dienstjaren}")
    print(f"premie is {premie}")

    familienaam = input("Geef jouw familienaam in: ")

print(f"De totaal te betalen premie is {totaal_premie}")
print(f"De hoogste premie is {hoogste_premie}")