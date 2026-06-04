minErtek = int(input("Kérem az első pozitív egész számot: "))
maxErtek = int(input("Kérem a második pozitív egész számot: "))

vanE = False

if maxErtek < minErtek:
    maxErtek, minErtek = minErtek, maxErtek

for elem in range(minErtek, maxErtek + 1):
    if elem % 7 == 0 and elem % 2 == 0:
        vanE= True
        print(elem)

if not vanE:
    print("***nem található megfelelő szám***")