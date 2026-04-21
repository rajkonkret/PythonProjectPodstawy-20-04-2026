# warunki
# instrukcje warunkowe
#  instrukcje sterowanie przepływem programu
# if
# w zależności od warunku wykona jeden lub drugi blok programu
# wyrażenie w warunku musi zwrócic typ bool

odp = True

if odp: print("test")  # test

if odp:
    print("Test")  # Test
# debugger - narzędzie do wykonywania kodu krok po kroku, ułątwia wyszukiwanie błedów
# pułapka - miejsce gdzie program ma się zatrzymać
odp = False
if odp:  # blok programu wykonany gdy warunek jest spełniony -> True
    print("Brawo")
    # print("Brawo") # IndentationError: unexpected indent
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza częśc programu")

odp = "Radek"
if odp:
    print("Dane zostały wczytane")
# Dane zostały wczytane

if odp == "Radek":  # == porównanie
    print('Jestem Radek')
# Jestem Radek

odp = 0
if odp:
    print("Działa")
else:  # w innym przypadku, wartość domyślna
    print("Zero -> False")
# Zero -> False

a = "Radek"
# jezeli długość tekstu jest większa niż 3 to wypisać:
# Długość wynosi: wstawic długość, więcej niż 3

if len(a) > 3:
    print(f"Długość wynosi: {len(a)}, więcej niż 3")
# Długość wynosi: 5, więcej niż 3

n = len(a)
if n > 3:
    print(f"Długość wynosi: {n}, więcej niż 3")
# Długość wynosi: 5, więcej niż 3

# operator morsa, walrus operator
if (n := len(a)) > 3:
    print(f"Długość wynosi: {n}, więcej niż 3")
