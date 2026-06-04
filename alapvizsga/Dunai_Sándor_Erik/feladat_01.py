minErtek = int(input("Kérem az első pozitív egész számot: "))
maxErtek = int(input("Kérem a második pozitív egész számot: "))

if minErtek > maxErtek:
    minErtek, maxErtek = maxErtek, minErtek

ilyenSzam = False
for elem in range(minErtek, maxErtek, +1):
    if elem % 2 == 0 and elem % 7 == 0:
        print(elem)
        ilyenSzam = True

if not ilyenSzam:
    print("**Nem található megfelelő szám.**")