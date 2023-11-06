a, b = 1, 1

print(a, end="\t")

while b < 1501:
    print(b, end="\t")
    a, b = b, a + b
