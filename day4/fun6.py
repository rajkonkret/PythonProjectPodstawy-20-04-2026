# napisać funkcję obliczającą średnią
def srednia(name=None, *cyfry):  # dowolna ilosc argumentów przekazaych po pozycji
    print(cyfry)  # (1, 2, 3, 4)

    count = len(cyfry)

    suma = 0
    suma_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = suma_p / count
    except Exception as e:
        print("Błąd:", e)
    else:  # tylko gdy nie ma błędu
        print(f"Średnia dla ucznia: {name} wynosi: {avg}")
        print(f"Średnia dla ucznia: {name} wynosi: {avg_p}")
    finally:
        print('kolejny uczeń')


srednia()
srednia("Radek", 2, 3, 4)  # ("Radek", 2, 3, 4)
# name, *cyfry = ("Radek", 2, 3, 4)
# ()
# Błąd: division by zero
# kolejny uczeń
# (2, 3, 4)
# Średnia dla ucznia: Radek wynosi: 3.0
# Średnia dla ucznia: Radek wynosi: 3.0
# kolejny uczeń
