import random

class Cake:
	OlcsoLaktozmentes = 0
	def __init__(self, nev, szeletekSzama, ar, laktoz):
		self.nev = nev
		self.szeletekSzama = szeletekSzama
		self.ar = ar
		self.laktoz = laktoz
	
	def olcsoLaktozmentesSzamlalas(self):
		if self.laktoz == "nem" and self.ar < 1400:
			Cake.OlcsoLaktozmentes += 1 
	
	def rendeles(self, darab):
		osszeg = darab * int(self.ar)
		print(f"Rendelés: {darab} {self.nev}. Részösszeg: {osszeg}")
		return osszeg
	
cakes = []

with open("list_of_cakes.txt", encoding="utf-8") as f:
	for elem in f:
		lista = elem.strip().split(";")
		torta = Cake(lista[0], lista[1], int(lista[2]), lista[3])
		torta.olcsoLaktozmentesSzamlalas()
		cakes.append(torta)

print(f"Olcsó laktózmentes torták száma: {Cake.OlcsoLaktozmentes}")

def osszrendeles(lista):
	random.shuffle(cakes)
	ossz = 0
	for i in range(3):
		ossz += cakes[i].rendeles(lista[i])
	print(f"Összesen fizetendő: {ossz}")

darabszamok = [1, 2, 1]
osszrendeles(darabszamok)