cakes = []

with open("list_of_cakes.txt", encoding="utf8") as f:
    for elem in f:
        lista = elem.strip().split(";")
        cakes.append(lista)

huszonnegyLaktozmentesOsszege = len(cakes)
print(f"Feladat: A torták száma: {huszonnegyLaktozmentesOsszege}")