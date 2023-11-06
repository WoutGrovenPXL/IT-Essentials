a = int(input("Geef geheel getal a in: "))
b = int(input("Geef geheel getal b in: "))
code = int(input("Geef code in (1=optelling;2=aftrekking;3=vermenigvuldiging;4=kwadraat van a;5=kwadraat van b): "))

uitkomst = 0

if code == 1:
    uitkomst = a + b
elif code == 2:
    uitkomst = a - b
elif code == 3:
    uitkomst = a * b
elif code == 4:
    uitkomst = b ** a
elif code == 5:
    uitkomst = a ** b
else:
    uitkomst = "foutieve code"

print("De 2 getallen zijn ", a, " en ", b, " en het resultaat is ", uitkomst)