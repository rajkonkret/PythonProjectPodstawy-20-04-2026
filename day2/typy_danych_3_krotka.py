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
