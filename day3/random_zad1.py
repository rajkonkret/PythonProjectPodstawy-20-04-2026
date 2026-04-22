import random
from calendar import prweek

# działania na liczbach losowych

#  """Return random integer in range [a, b], including both end points.
#         """
print(random.randint(1, 100))  # int, od 1 do 100

print(random.randrange(1, 100))  # int, od 1 do 99
print(random.randrange(5))  # od 0 do 4

print(random.random())  # float, od 0 do 0.9999999 ->  0.600380112524912
print(random.random() * 7)  # float, od 0 do 6.9999999 ->  1.5768172948473143

lista = [67, 45, 32, 68, 90, 42, 49]
print(lista[random.randrange(len(lista))])  # liczba 49

print(random.choice(lista))  # 49 element z listy, losuje jeden element

for _ in range(6):
    lista_kul = list(range(1, 50))
    # print(lista_kul)
    kula = random.choice(lista_kul)
    lista_kul.remove(kula)
    print(kula)
