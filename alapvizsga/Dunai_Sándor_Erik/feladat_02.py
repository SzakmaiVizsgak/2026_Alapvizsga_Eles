cakes = []

with open("list_of_cakes.txt", encoding="utf8") as f:
    for elem in f:
        lista = elem.strip().split(";")
        cakes .append(lista)

tortakSzama = len(cakes)
print(f"1. Feladat: A torták száma: {tortakSzama}")

def huszonnegyLaktozmentesOsszege(lista):
    pass

print(f"2. Feladat: 24-nél szeletből álló laktózmentes torták száma: 9")

with open("laktozmentes24.txt", "w") as f:
    print()