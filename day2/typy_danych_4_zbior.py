# zbior (set) - przechowują unikalne wartości
# nie zachowuje kolejności przy dodawaniu elemntów
# nie posiada indeks

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(type(zbior))  # <class 'set'>
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}, zmiana kolejności

lista_sort = sorted(zbior)
print(lista_sort)  # [11, 22, 33, 44, 55, 66, 777]

lista_sort = list(zbior)
lista_sort.sort()
print(lista_sort)
