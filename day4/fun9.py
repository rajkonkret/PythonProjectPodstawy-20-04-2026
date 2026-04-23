# funkcja lambda
# skrócony zapis funkcji
# lambda zawsze zwraca wynik -> return
# funkcja anonimowa

def odejmij(a, b):
    return a - b


print(odejmij(10, 8))  # 2

odejmij2 = lambda a, b: a - b
print(odejmij2(10, 8))  # 2

# zamien na lambda
# def oblicz_vat(kwota, vat=23):
#     return kwota * (100 + vat) / 100

oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
# 1230.0
# 1080.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")

print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie danych
lista = [1, 2, 14, 24, 50, 67, 80, 100, 200, 500]

# stworzyc listę, do listy zapisać elementy tej listy, pomnożone * 2
l1 = []
for i in lista:
    l1.append(i * 2)
print(l1)  # [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

l2 = [i * 2 for i in lista]
print(l2)  # [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]


def zmien(x):
    return x * 2


l3 = []
for i in lista:
    l3.append(zmien(i))
print(l3)
# [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

# map() - wykonuje funkcję na kolejnych argumentach kolekcji
# funkcje wyższego rzędu, jako argument przyjmuje inną funkcję

print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

# użycie lambdy jako funkcja anonimowa
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 5, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 6, lista))}")
# Zastosowanie map(): [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]
# Zastosowanie map(): [4, 8, 56, 96, 200, 268, 320, 400, 800, 2000]
# Zastosowanie map(): [5, 10, 70, 120, 250, 335, 400, 500, 1000, 2500]
# Zastosowanie map(): [6, 12, 84, 144, 300, 402, 480, 600, 1200, 3000]

# filtrowanie danych
l4 = []
for i in lista:
    if i < 3:
        l4.append(i)

print(l4)  # [1, 2]

# filter() - zwraca element spełniający warunek
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 5, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 100, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 200, lista))}")
# Zastosowanie filter(): [1, 2]
# Zastosowanie filter(): [1, 2]
# Zastosowanie filter(): [1, 2]
# Zastosowanie filter(): [200, 500]
# Zastosowanie filter(): [500]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 100, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 100, lista))}")
# Zastosowanie filter(): [14, 24, 50, 67, 80]
# Zastosowanie filter(): [14, 24, 50, 67, 80]