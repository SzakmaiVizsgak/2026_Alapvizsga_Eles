cake = []

with open("list_ofcakes.txt", encoding="utf-8") as f:
    for elem in f:
       lista = elem.strip().split()
       lista.append(cake)

tortak = len(cake)
print(f"A torták száma: {tortak}")

def huszonnegyLaktozMentesOsszege(lista):
    pass