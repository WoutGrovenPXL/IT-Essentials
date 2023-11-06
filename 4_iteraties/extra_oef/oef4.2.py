naam = input("Geef de naam van de student in: ")

while not (naam == "xx" or naam == "XX"):
    behaald_percentage = int(input("Geef het percentage van de student jan in: "))

    while behaald_percentage < 0 or behaald_percentage > 100:
        if behaald_percentage < 0:
            print("Fout! het getal moet minstens 0 zijn.")
        elif behaald_percentage > 100:
            print("Fout! het getal mag maximum 100 zijn.")

        behaald_percentage = int(input("Geef het percentage van de student jan in: "))

    if behaald_percentage < 60:
        graad = "onvoldoende"
    elif (behaald_percentage >= 60) and (behaald_percentage < 70):
        graad = "voldoende"
    elif (behaald_percentage >= 70) and (behaald_percentage < 80):
        graad = "onderscheiding"
    elif (behaald_percentage >= 80) and (behaald_percentage < 85):
        graad = "grote onderscheiding"
    else:
        graad = "grootste onderscheiding"

    print(f"De graad van student {naam} is {graad}")

    naam = input("Geef de naam van de student in: ")
