bedrag = int(input("Geef het bedrag in centen in: "))

bedrag_200 = bedrag // 200
rest_200 = bedrag % 200

bedrag_100 = rest_200 // 100
rest_100 = bedrag_100 % 100

bedrag_50 = rest_100 // 50
rest_50 = bedrag_50 % 50

bedrag_20 = rest_50 // 20
rest_20 = bedrag_20 % 20

bedrag_10 = rest_20 // 10
rest_10 = bedrag_10 % 10

bedrag_5 = rest_10 // 5
rest_5 = bedrag_5 % 5

bedrag_2 = rest_5 // 2
rest_2 = bedrag_2 % 2

bedrag_1 = rest_2 // 1
rest_1 = bedrag_1 % 1

print(bedrag_200, " van 2 EUR - ", bedrag_100, " van 1 EUR - ", bedrag_50, " van 50 cent - ", bedrag_20,
      " van 20 cent - ", bedrag_10, " van 10 cent - ", bedrag_5, " van 5 cent - ", bedrag_2, " van 2 cent - ", bedrag_1,
      " van 1 cent")
