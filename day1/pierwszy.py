# pep8 -  formatowanie
# snake_case - konwencja nazewnicza
import sys

print("Hello World")  # wypisz/wydrukuj
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

print(30 + 89)  # 119
print(type(39))  # <class 'int'> - całkowite

print(sys.int_info)
# sys.int_info(bits_per_digit=30,
# sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)

# print("39" + 30) # TypeError: can only concatenate str (not "int") to str
# silne typowanie - nie zmainia typów

# rzutowanie typów
print(int("39"))  # rzutowanie na typ integer
print(int("39") + 39)  # 78
print("39" + str(39))  # 3939

print("'xxx'")  # 'xxx'
print('"xxx"')  # "xxx"

# zmienna
# pudełko, wagonik na dane

# typowanie dynamiczne
name = "Radek"
print(name)  # Radek
print(type(name))  # <class 'str'>

name = 90
print(name)  # 90
print(type(name))  # <class 'int'>

print(50 * "90")
# 9090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090909090

# podpowiedzi typów
name: str = "Radek"
print(name)  # Radek
name = 90
print(name)  # 90
print(type(name)) # <class 'int'>
