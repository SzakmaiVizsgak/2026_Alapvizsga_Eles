cakes = []

with open("list_of_cakes.txt", encoding="utf-8") as f:
    for elem in f:
        lista = elem.strip().split(";")
        cakes.append(lista)

cakesNumber = len(cakes)
print(f"1. Feladat: A torták száma: {cakesNumber}")

def huszonnegyLaktozmentesOsszege(lista):
    szamlalo = 0
    for elem in lista:
        if int(elem[1]) == 24 and str(elem[3]) == "nem":
            szamlalo += 1
    return szamlalo

laktozmentes24 = huszonnegyLaktozmentesOsszege(cakes)
print(f"2. Feladat: 24 szeletből álló laktózmentes torták száma: {laktozmentes24}")

with open("laktozmentes24.txt", "w", encoding="utf-8") as f:
    f.write(f"2. Feladat: 24 szeletből álló laktózmentes torták száma: {laktozmentes24}")