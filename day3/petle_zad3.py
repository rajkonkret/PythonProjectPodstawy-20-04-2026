# while  - pętla sterowana warunkiem

# # pętla nieskońćzona
# while True:
#     print("Komunikat")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerwanie pętli

print(50 * "-")
print(licznik)

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")
# --------------------------------------------------
# 11
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!

# password = input("Podaj hasło:")
# while password != 'secret':  # != - różne
#     password = input("Podaj ponownie")
# Podaj hasło:asad
# Podaj ponownieaDSAD
# Podaj ponownieaaS
# Podaj ponownieWQE
# Podaj ponownieDSDAFS
# Podaj ponownieSECRET
# Podaj ponowniesecret

# while (password := input("Podaj hasło:")) != 'secret':
#     pass
# Podaj hasło:asad
# Podaj hasło:asda
# Podaj hasło:secret

# usunąc liczby 5 z listy
my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]

number_to_remove = 5
while number_to_remove in my_list:
    my_list.remove(number_to_remove)

print(my_list)  # [1, 2, 3, 4, 6] usunięete duplikaty, zachowana kolejność

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]

# zwraca nową listę
# bez utraty kolejności
print(dict.fromkeys(my_list))
# {1: None, 5: None, 2: None, 3: None, 4: None, 6: None}

print(list(dict.fromkeys(my_list)))  # [1, 5, 2, 3, 4, 6]
