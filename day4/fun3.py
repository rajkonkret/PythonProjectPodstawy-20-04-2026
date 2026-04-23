a = 10
b = 10


def dodaj():
    a = 7  # zmienne lokalne, widoczne tylko wewnątrz funkcji
    b = 8
    print(a + b)


print(f"Wartoś a z góry (globalna): {a}")  # Wartoś a z góry (globalna): 10
dodaj()  # 15
print(f"Wartoś a z góry (globalna): {a}")  # Wartoś a z góry (globalna): 10
