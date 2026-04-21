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

# ctrl /
# podatek = 0
# zarobki = int(input("Podaj zarobki:"))
#
# if zarobki < 10_000:
#     podatek = 0
# # elif zarobki >= 10_000 and zarobki < 40_000:
# # elif 10_000 <= zarobki < 40_000:
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
#
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi: {zarobki * podatek} pln.")
# dodac podatek 20%, dla zarobków od 10000 do 39999.99

sum_zam = 150
if sum_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi: {rabat}")  # Rabat wynosi: 25

# operator warunkowy
rabat = 25 if sum_zam > 100 else 0
print(f"Rabat wynosi: {rabat}")  # Rabat wynosi: 25

# napisac test z...
# trzy pytania
# punktacja

punkty = 0
odp = input("Podaj rok Chrztu Polski: ")  # -> str
if odp.strip().casefold() == '966':  # == porównanie
    print("Odpowiedź prawidłowa")
    # punkty = punkty + 1
    punkty += 1
else:
    print("Masz w ksiażce na stronie 26")
# Podaj rok Chrztu Polski: 966
# Odpowiedź prawidłowa

odp = input("Jaka jest stolica Polski: ")  # -> str
if odp.strip().casefold() == 'Warszawa'.casefold():  # == porównanie
    print("Odpowiedź prawidłowa")
    punkty += 1
else:
    print("Masz w ksiażce na stronie 29")

odp = input("Jaka jest dzień tygodnia: ")  # -> str
if odp.strip().casefold() == 'wtorek':  # == porównanie
    print("Odpowiedź prawidłowa")
    punkty += 1
else:
    print("Masz w kalendarzu")

print(f"Zdobyłeś: {punkty} pkt.")
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

# Podaj rok Chrztu Polski: 966
# Odpowiedź prawidłowa
# Jaka jest stolica Polski: warszawa
# Odpowiedź prawidłowa
# Jaka jest dzień tygodnia: wtorek
# Odpowiedź prawidłowa
# Zdobyłeś: 3 pkt.