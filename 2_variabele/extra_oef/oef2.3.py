INCH = 0.0254
PI = 3.14

diameter_wiel = float(input("Geef de diameter van je wiel in (inches): "))
afstand = float(input("Geef de afstand die je wil afleggen (m): "))

print("Het aantal omwentelingen dat je wiel moet maken om ", afstand, " meter af te leggen is ",
      afstand / (diameter_wiel * PI * INCH))
