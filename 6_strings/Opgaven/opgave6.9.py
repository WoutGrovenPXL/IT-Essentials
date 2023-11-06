def main():
    string = "The quick brown fox jumps over de lazy cat."
    string = string.replace("d", "th")
    string = string.replace("cat", "dog")

    print(string)


if __name__ == "__main__":
    main()
