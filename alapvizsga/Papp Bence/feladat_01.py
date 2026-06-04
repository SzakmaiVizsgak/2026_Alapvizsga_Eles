minErtek = int(input("Kérem az első pozitív számot."))
maxErtek = int(input("Kérem a masodik pozitív egész számot."))

if minErtek > maxErtek:
    minErtek, maxErtek = maxErtek, minErtek

vanE = False
for elem in range(minErtek,maxErtek + 1):
    if elem % 5 == 0 and elem % 10 == 0: 
        print(elem)

        vanE = True
if not vanE:
    print("**Nem található megfelelő szám**")
    