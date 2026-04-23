# funkcja - wydzielony fragment kodu, można wykonać w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana
# żeby funkcja się uruchomiła musimy ją wywołać

a = 6
b = 8


# funkcje nie zwracają wartości
# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # argumenty obowiązkowe
    print(a + b)


# ominięcie problemu braku przeciążania funkcji liczbą argumentów
# argumenty o wartosci domyslnej
def odejmij(a, b, c=0):
    print(a - b - c)


# wywołanie funkcji
dodaj()  # 14

# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(7, 9)  # 16

# argumenty po pozycji
odejmij(1, 2)  # -1
odejmij(1, 2, 3)  # -4

# argumenty po nazwie
odejmij(b=90, a=87)  # -3
odejmij(c=87, b=76, a=89)  # -74

# mieszane
odejmij(1, 2, c=89)  # -90
dodaj2(1, b=90)  # 91

# argumenty pozycyjne muszą byc przed nazwanymi
# SyntaxError: positional argument follows keyword argument
# odejmij(a=10, 1, 2)

# print(dodaj() + dodaj2(6, 90))
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
