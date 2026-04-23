# json -> {"name":"John", "age":30, "car":null}
# json - dane typu klucz wartość
# typ danych do wymiany pomiedzy klient-serwer
# odpowiednikiem jsona w pythonie jest słownik
# {
#         "description": "\u201eIteration\u201d to proces przechodzenia przez elementy obiektu iterowalnego, takiego jak lista lub krotka.",
#         "example": "print(\"Przyk\u0142ad do: Co to jest \u201eiteration\u201d w Pythonie?\")",
#         "id": 31,
#         "level": "podstawowy",
#         "term": "Co to jest \u201eiteration\u201d w Pythonie?"
#     }

import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(person_dict)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>
