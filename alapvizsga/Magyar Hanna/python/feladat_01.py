minErtek = int(input("Kérem az első pozitív egész számot: "))
maxErtek = int(input("Kérem a második pozitív egész számot: "))

if maxErtek < minErtek:
    maxErtek, minErtek = minErtek, maxErtek

vanE = False

for elem in range (minErtek, maxErtek + 1):
    if elem % 7 == 0 and elem % 2 == 0:
        print(elem)
        vanE = True

if not vanE:
    print("**Nem található megfelelő szám.**")