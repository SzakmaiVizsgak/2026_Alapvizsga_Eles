minErtek = int(input("Kérem az első számot"))
maxErtek = int(input("Kérem a második számot"))
if maxErtek < minErtek:
  minErtek, maxErtek = maxErtek, minErtek

vanE = False

for elem in range(minErtek, maxErtek +1):   
 if elem % 5 == 0 and elem % 2 == 0:
  print(elem) 
  vanE = True
  
if not vanE:
 print(**"Nem található megfelelő szám**")