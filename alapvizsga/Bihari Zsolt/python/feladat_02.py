cakes = []

with open('list_of_cakes.txt', encoding="UTF-8") as f:
    for elem in f:
        lista = elem.strip().split(";")
        cakes.append(lista)

tortakSzama = len(cakes)
print(f"1.Feladat : A torták száma: {tortakSzama}")