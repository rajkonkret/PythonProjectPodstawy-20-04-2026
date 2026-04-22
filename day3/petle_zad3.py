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

while (password := input("Podaj hasło:")) != 'secret':
    pass
# Podaj hasło:asad
# Podaj hasło:asda
# Podaj hasło:secret
