# funkcje zwracające wynik
# kończą się: return

a = 9
b = 98


def dodaj():
    return a + b


def dodaj2(a, b):  # argumenty obowiązkowe
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


print(dodaj())  # 107

print(dodaj2(5, 8))  # 13
print(dodaj2(b=9, a=87))  # 96

print(odejmij())
print(odejmij(1))
print(odejmij(1, 2))

wynik = odejmij(6, 8, 24)
print("Wynik:", wynik)  # Wynik: -26


def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


print(oblicz_vat(1000))  # 1230.0
print(oblicz_vat(1000, 8))  # 1080.0
print(oblicz_vat(vat=15, kwota=1000))  # 1150.0

zm = oblicz_vat(1000)
print(type(zm))  # <class 'float'>
print(zm)  # 1230.0
if zm == 1230:
    print("Ok")  # Ok

print(dodaj() + odejmij(1, 4, 6))
# 98
