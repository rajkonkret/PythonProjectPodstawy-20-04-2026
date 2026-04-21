# krotka (tupla) - lista tylko do odczytu, niemutowalna
# pozwala efektywniej zarządzac pamięcią
# krotka jednoelementowa, stała, szczegolny przypadek zmiennej

tupla_imiona = "Zenek", "Marek", 'Radek', "Ania"
print(type(tupla_imiona))  # <class 'tuple'>
print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')

# tupla_liczby = (43, 55, 22.34, 11, 200)
tupla_liczby = 43, 55, 22.34, 11, 200
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>

tupla_jeden = 45,
print(tupla_jeden)  # (45,)
print(type(tupla_jeden))  # <class 'tuple'>

# przy tulach jednoeleemntowych PEP8 zaleca nawiasy ()
tupla_jeden = (45,)
print(tupla_jeden)  # (45,)
print(type(tupla_jeden))  # <class 'tuple'>

# usunięcie całej tupli
del tupla_jeden
# print(tupla_jeden) # NameError: name 'tupla_jeden' is not defined

# tupla jest niemutowalna
# tupla_liczby[0] = 123 # TypeError: 'tuple' object does not support item assignment

print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')
# count, index
print(tupla_imiona.index("Radek"))  # index numer 2
print(tupla_imiona.count("Radek"))  # występuje 1 raz

print(len(tupla_imiona))  # długośc 4

tup = 1, 2
print(type(tup))  # <class 'tuple'>

# a - pierwsza wartośc, b - druga wartość
a = tup[0]
b = tup[1]
print(a, b)  # 1 2

# rozpakowanie tupli
a, b = 1, 2  # tupla w pamięci
print(a, b)  # 1 2

a, b = tup
print(a, b)  # 1 2

a, b = b, a  # zamiana miejscami wartosci zmiennych
print(b, a)  # 1 2

# ('Zenek', 'Marek', 'Radek', 'Ania')
# name1, name2, name3
# name1, name2, name3 = tupla_imiona # ValueError: too many values to unpack (expected 3, got 4)
name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)  # Zenek Marek ['Radek', 'Ania']

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  #
# Zenek ['Marek', 'Radek'] Ania

*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)  # ['Zenek', 'Marek'] Radek Ania
