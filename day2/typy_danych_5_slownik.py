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
