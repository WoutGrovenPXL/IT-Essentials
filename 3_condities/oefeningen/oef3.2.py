brutoloon = float(input("Geef het brutoloon: "))

jaarlijkse_bijdrage = 0
vakantiegeld = brutoloon * 0.05

if vakantiegeld >= 350:
    jaarlijkse_bijdrage = 350 * 0.08
else:
    jaarlijkse_bijdrage = vakantiegeld * 0.08

print("Het brutoloon van deze werknemer is ", brutoloon)
print("Het vakantiegeld van deze werknemer is ", vakantiegeld)
print("De jaarlijkse bijdrage van deze werknemer is ", jaarlijkse_bijdrage)