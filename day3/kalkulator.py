# napisać apliakcję kalkulator
# while True
# menu z opcjami
# wyświetlić ładnie wynik 5 + 9 = 14
# obsłużyć wyjątki
while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)

    odp = input("Podaj wybraną opcję:")  # str

    # if odp == "5":
    #     break

    if odp not in ["1", "2", "3", "4"]:
        break

    try:
        a = float(input("Podaj pierwszą liczbę:"))
        b = float(input("podaj drugą liczbę:"))

        if odp == "1":
            print(f"Dodawanie: {a} + {b} = {a + b}")
        elif odp == "2":
            pass
        elif odp == "3":
            pass
        elif odp == "4":
            print(f"Dzielenie: {a} / {b} = {a / b}")
    except ZeroDivisionError:
        print("Bład! Nie dziel przez zero!")
    except Exception as e:  # każdy inny błąd
        print("Bład:", e)
    finally:  # wykona się zawsze
        print("Obliczenia zostały wykonane")

print(50 * "-")
wyr = input("Podaj wyrażenie  do obliczenia:")
print(eval(wyr))
# Podaj wyrażenie  do obliczenia:>? 4+6
# 10
a = float(input("Podaj pierwszą liczbę:"))
b = float(input("podaj drugą liczbę:"))
znak = input("Wprowadź znak: (+,-,*,/)")
wyr = f"{a} {znak} {b}"
print(eval(wyr))
# Podaj pierwszą liczbę:>? 1
# podaj drugą liczbę:>? 2
# Wprowadź znak: (+,-,*,/)>? +
# 3.0
print(eval("5 + 7"))
# print(eval("5 + 7"))
# 12
