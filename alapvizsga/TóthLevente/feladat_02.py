cakes = []

with open("list_of_cakes.txt", encoding="utf-8") as f:
    for elem in f:
        list = elem.strip().split(";")
        cakes.append(list)

print(f"1. Feladat: A torták száma: {len(cakes)}")

def huszonnegyLaktozmentesOszzege(lista):
    pass

