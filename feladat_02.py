cakes = []

with open("list_of_cakes.txt", encoding="utf-8") as f:
	for elem in f:
		lista = elem.strip().split(";")
		cakes.append(lista)

cakesSzama = len(cakes)
print(f"1. Feladat: A torták száma: {cakesSzama}")

def huszonnegyLaktozmentesOsszege(lista):
	szamlalo = 0
	for elem in lista:
		if int(elem[1]) == 24 and elem[3] == "nem":
			szamlalo += 1
	return szamlalo

darabszam = huszonnegyLaktozmentesOsszege(cakes)
kiir = f"2. Feladat: 24-nél szeletből álló laktózmentes torták száma: {darabszam}"
print(kiir)

with open("laktozmentes24.txt", "w", encoding="utf-8") as f:
	f.write(kiir)
