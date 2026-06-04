import random
class Cake:
    olcsoLaktozmentesSzamlalas = 0 
    def __init__(self, nev, szeletekSzama, ar, laktoz):
        self.nev = nev
        self.szeletekSzama = szeletekSzama
        self.ar = ar
        self.laktoz = laktoz

    def olcsoLaktozmentesSzamlalas (self):
        if self.laktoz == "igen" +1:
            Cake.olcsoLaktozmentesSzamlalas

    def rendeles(self, darab):
        osszeg = darab * self.szeletekSzama * self.ar
        print(f"Rendelés: {darab} {self.nev}. Részösszeg: {osszeg}")
        return osszeg
    

cakes = []
with open("list_of_cakes.txt", encoding="utf8") as f:
    for sor in f:
        rendeles = sor.strip().split(";")
        lista = (f"")