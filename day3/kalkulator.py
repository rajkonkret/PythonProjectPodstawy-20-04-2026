# napisać apliakcję kalkulator
# while True
# menu z opcjami
# wyświetlić ładnie wynik 5 + 9 = 14
# obsłużyć wyjątki
while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    5. Koniec
    """)

    odp = input("Podaj wybraną opcję:")  # str

    if odp == "5":
        break

    a = float(input("Podaj pierwszą liczbę"))
    b = float(input("podaj drugą lizcbę"))

    if odp == "1":
        pass
    elif odp == "2":
        pass
