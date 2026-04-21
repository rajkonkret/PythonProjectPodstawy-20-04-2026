# słownik - para klucz:wartosc
# {"user" : "Radek"}
# klucze nie mogą się powtarzac
# odpowiednik jsona
# {"name":"John", "age":30, "car":null}

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = dict()
print(dictionary_1)  # {}
print(type(dictionary_1))  # <class 'dict'>

# dodanie elementów do słownik
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}

# dodac klucz wiek
dictionary['wiek'] = 50
print(dictionary)  # {'imie': 'Radek', 'wiek': 50}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 50])
# dict_items([('imie', 'Radek'), ('wiek', 50)])

# nadpisanie wartości
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 50}

# wypisanie wartości dla klucza
print(dictionary['imie'])  # Tomek

dictionary['imie'] = ['Radek', "Tomek", "Magda"]
print(dictionary)  # {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50}

# wypisać Tomka
print(dictionary['imie'])  # ['Radek', 'Tomek', 'Magda'] [1]
print(dictionary['imie'][1])  # Tomek

print(dictionary['imie'][1].lower())  # tomek
print(dictionary['imie'][::-1])  # ['Magda', 'Tomek', 'Radek']

dictionary_radek = {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50}
print(dictionary_radek)  # {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50}

# print(dictionary_radek['Imie'])  # KeyError: 'Imie'
print(dictionary['Imie'.lower()])  # ['Radek', 'Tomek', 'Magda']

print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default

name1 = 'GROSS'
name2 = "groß"  # ß -> ss

print(name1.lower() == name2.lower())  # False
"""Return a version of the string suitable for caseless comparisons."""
print(name1.casefold() == name2.casefold())  # True

dictionary.update({"data": "12-12-2028"})
print(dictionary)
# {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 50, 'data': '12-12-2028'}

# [('imie', 'Radek'), ('wiek', 50)] - lista krotek
dict_small = {'x': 2}
dict_small.update([("y", 3), ("z", 6)])  # dane jako lista krotek
print(dict_small)  # {'x': 2, 'y': 3, 'z': 6}

# input() - możliwość wprowadzenia danych do komputera np.:  z klawiatury

# input zwraca str
# tekst = input("Podaj imie:")
# print(tekst)
# # Podaj imie:Radek
# # Radek

# ctrl /
# napisac apliakcje kalkulator
# a = int(input("Podaj pierwszą liczbę:"))
# b = input("Podaj drugą liczbę:")
# print(a + float(b))
# # Podaj pierwszą liczbę:4
# # Podaj drugą liczbę:5
# # 9.0
#
# # eval()
# print(eval("5 * 8"))  # 40

# napisac apliakcję słownik pol-ang
# pol_ang = {'pies': "dog", "kot": 'cat', "dach": "roof"}
# print("Znam takie słowa:", pol_ang.keys())
# odp = input("Podaj słówko do przetłumaczenia:")
# print(f"""
# Prawidłowa odpowiedź dla: {odp}
# to: {pol_ang.get(odp.strip().casefold(), "nie ma")}
# """)
# Podaj słówko do przetłumaczenia:kot
#
# Prawidłowa odpowiedź dla: kot
# to: cat

# \N{name} - Znak Unicode o podanej nazwie
print("\N{LATIN SMALL LETTER SHARP S}")  # ->  ß
