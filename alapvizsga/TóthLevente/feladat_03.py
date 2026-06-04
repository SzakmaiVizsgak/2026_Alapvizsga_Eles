class Cake:
    def __init__(self, nev, szeletekSzama, ar, laktoz):
        self.nev = nev
        self.szeletekSzama = szeletekSzama
        self.ar = ar
        self.laktoz = laktoz

        for elem in range (ar, laktoz):
            list = elem.strip().split(";")
            for elem in range(list):
                if ar < 1400 and laktoz == "igen":
                    print(f"Olcsó laktózmentes torták száma: {len(elem)}")