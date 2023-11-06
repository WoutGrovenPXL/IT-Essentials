GEWICHT_TOV_MAAN = 0.165
GEWICHT_TOV_JUPITER = 2.537
GEWICHT_TOV_MARS = 0.378

for i in range(50, 121, 5):
    print(f"Aarde: {i}")
    print(f"Maan: {i * GEWICHT_TOV_MAAN}")
    print(f"Jupiter: {i * GEWICHT_TOV_JUPITER}")
    print(f"Mars: {i * GEWICHT_TOV_MARS}")
    print("\n")