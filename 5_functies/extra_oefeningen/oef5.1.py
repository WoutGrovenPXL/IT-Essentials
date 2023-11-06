def main():
    def gregory_leibniz_pi_approximation(terms):
        pi_approximation = 0.0

        for i in range(terms):
            numerator = 4 if i % 2 == 0 else -4  # Wissel tussen positieve en negatieve termen
            denominator = 2 * i + 1
            pi_approximation += numerator / denominator

        return pi_approximation

    # Voorbeeldgebruik:
    num_terms = 100000  # Pas het aantal termen naar wens aan
    approximated_pi = gregory_leibniz_pi_approximation(num_terms)
    print("Benaderde waarde van π:", approximated_pi)


if __name__ == "__main__":
    main()