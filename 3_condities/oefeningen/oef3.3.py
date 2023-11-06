vertrek_uur = int(input("Geef vertrekuur: "))
vertrek_minuut = int(input("Geef vertrekminuten: "))
duur_minuten = int(input("Geef de duur in minuten: "))

totaal_vertrek_minuten = (vertrek_uur * 60) + vertrek_minuut
aankomst_tijd = totaal_vertrek_minuten + duur_minuten

aankomst_uur = aankomst_tijd // 60
aankomst_minuten = aankomst_tijd % 60

if aankomst_uur >= 24:
    aankomst_uur %= 24

print("Je komt aan om ", aankomst_uur, ":", aankomst_minuten, "h")




