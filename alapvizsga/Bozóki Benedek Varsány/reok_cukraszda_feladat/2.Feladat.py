cakes = []

with open("list_of_cakes.txt", encoding="utf-8")as f:
    for elem in f:
        
        lista = elem.strip().split(";")
        cakes.append(lista)
        
cakesSzama = len(cakes)

print(f"1.feladat : torták száma {cakesSzama}")