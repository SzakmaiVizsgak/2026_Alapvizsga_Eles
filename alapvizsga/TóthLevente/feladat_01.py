minErtek = int(input("Kérem az első pozitív egész számot: "))
maxErtek = int(input("Kérem a második pozitív egész számot: "))

if minErtek > maxErtek:
    minErtek, maxErtek = maxErtek, minErtek

vanEIlyen = False

for elem in range(minErtek, maxErtek + 1):
    if elem % 2 == 0 and elem % 7 == 0:
        print(elem)
        vanEIlyen = True

if not vanEIlyen:
    print("**Nem található megfelelő szám.**")