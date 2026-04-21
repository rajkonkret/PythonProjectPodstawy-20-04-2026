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

# pusty zbior
zb2 = set()  # tylko i wyłącznie słówkiem set()
print(zb2)  # set() - pusty zbiór

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(33)
zbior.add(24)
zbior.add(24)
zbior.add(25)

print(zbior)
# {33, 66, 777, 11, 44, 18, 22, 55, 24, 25}

# usuniecie elemntu ze zbioru
zbior.remove(55)  # wartość elementu
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24, 25}

# pop()
print(zbior.pop())  # 33, usunie pierwszy element

zmienna = zbior.pop()
print(f"Zmienna: {zmienna}")  # Zmienna: 66
print('Zmienna:', zmienna)  # Zmienna: 66

zbior_copy = zbior.copy()
print(zbior_copy)  # {18, 22, 24, 777, 11, 44, 25}

print(id(zbior))
print(id(zbior_copy))
# 2174014872864
# 2174012117216
