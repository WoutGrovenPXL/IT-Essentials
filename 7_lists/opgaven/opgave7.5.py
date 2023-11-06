def tel_na(list, element):
    aantal = list.count(element)
    print(f"{element} komt {aantal} keer voor")

    list_indexen = []

    for i in list:
        list_indexen.append(list.index(element))

    for index in list_indexen:
        print(f"{element} komt voor op de index {index}")

def main():
    list = [5, 2, 3, 5, 1, 2, 3]
    tel_na(list, 5)

if __name__ == "__main__":
    main()
