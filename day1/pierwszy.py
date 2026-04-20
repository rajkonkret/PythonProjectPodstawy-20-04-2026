# pep8 -  formatowanie
# snake_case - konwencja nazewnicza
import sys

print("Hello World")
print('Witaj Świecie')
# blake8 - formater bardziej restrykcyjny

# ctrl /  - komentarz
# print('Hello world!")
#   File "C:\Users\CSComarch\PycharmProjects\PythonProjectPodstawy-20-04-2026\day1\pierwszy.py", line 8
#     print('Hello world!")
#           ^
# SyntaxError: unterminated string literal (detected at line 8)
# Process finished with exit code 1 bład w programie
print("Dalsza część")
# Hello World
# Witaj Świecie
# Dalsza część

# ctrl d - powiela linijke
print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")

print('"Radek"')  # "Radek"
print('Radek \"Radek\"')  # Radek "Radek"

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>, string, tekstowy

print("39" + "89")  # 3989, konkatenacja, łaczy teksty
print("Radek" + "1")  # Radek1

print(30 + 89) # 119
print(type(39)) # <class 'int'> - całkowite

print(sys.int_info)
# sys.int_info(bits_per_digit=30,
# sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)
