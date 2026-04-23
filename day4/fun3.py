a = 10
b = 10


def dodaj():
    a = 7  # zmienne lokalne, widoczne tylko wewnątrz funkcji
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj4():
    global a  # użyj zmiennej globalnej
    a = 7  # zmieniamy wartość zmiennej globalnej
    b = 90
    print(a + b)


def dodaj5():
    a = 7
    b = 9
    c = a + b
    print(c)


print(f"Wartoś a z góry (globalna): {a}")  # Wartoś a z góry (globalna): 10
dodaj()  # 15
print(f"Wartoś a z góry (globalna): {a}")  # Wartoś a z góry (globalna): 10
dodaj2()  # 20
print(f"Wartoś a z góry (globalna): {a}")  # Wartoś a z góry (globalna): 10
dodaj4()  # 97
print(f"Wartoś a z góry (globalna): {a}")  # Wartoś a z góry (globalna): 7
dodaj2()  # 17
print(f"Wartoś a z góry (globalna): {a}")  # Wartoś a z góry (globalna): 7
dodaj5()
# print(c) # NameError: name 'c' is not defined
print(f"Wartoś a z góry (globalna): {a}")  # Wartoś a z góry (globalna): 7
