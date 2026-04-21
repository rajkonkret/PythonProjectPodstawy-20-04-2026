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
