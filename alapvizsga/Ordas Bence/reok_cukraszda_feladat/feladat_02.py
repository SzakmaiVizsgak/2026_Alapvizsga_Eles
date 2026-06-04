cakes = []

with open("list_of_cakes.txt", encoding="utf8") as f:
    for elem in f:
        lista = elem.strip().split(";")
        cakes.append(lista)

tortakSzama = len(cakes)
print(f"A torták száma: {tortakSzama}")