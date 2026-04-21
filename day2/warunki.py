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
