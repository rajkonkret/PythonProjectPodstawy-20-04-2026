# kolekcje

# lista - przechowuje dowolną ilośc danych, różnego typu na raz
# zachowuje kolejnośc podczas dodawania elementów

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# dodawanie elementów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Marek")
lista.append("Sebastian")
lista.append("Anna")
lista.append("Magda")
print(lista)
# ['Radek', 'Tomek', 'Marek', 'Sebastian', 'Anna', 'Magda']

print(len(lista))  # 6 elementów

# ['Radek', 'Tomek', 'Marek', 'Sebastian', 'Anna', 'Magda']
#     0        1        2          3          4       5

print(lista[2])  # Marek
print(lista[4])  # Anna

# print(lista[10])  # IndexError: list index out of range

# ostatni element
print(lista[5])  # Magda
print(lista[len(lista) - 1])  # Magda
print(lista[-1])  # Magda
print(lista[-2])  # Anna
print(lista[-3])  # Sebastian

# ['Radek', 'Tomek', 'Marek', 'Sebastian', 'Anna', 'Magda']
#     0        1        2          3          4       5

# slicowanie - fragment listy
print(lista[0:3])  # ['Radek', 'Tomek', 'Marek'], 012
print(lista[:3])  # ['Radek', 'Tomek', 'Marek']

print(lista[2:])  # ['Marek', 'Sebastian', 'Anna', 'Magda'], z prawej zbiór otwarty
print(lista[2:5])  # ['Marek', 'Sebastian', 'Anna'], bez ostatniego

print(lista[2:10])  # ['Marek', 'Sebastian', 'Anna', 'Magda']

print(lista[12:26])  # []

print(lista[:])
# ['Radek', 'Tomek', 'Marek', 'Sebastian', 'Anna', 'Magda']

# ['Radek', 'Tomek', 'Marek', 'Sebastian', 'Anna', 'Magda']
#     0        1        2          3          4       5
#     -6       -5      -4          -3        -2       -1
print(lista[-2:0])  # [] -> [4:0]
print(lista[0:-2])  # [0:4] -> ['Radek', 'Tomek', 'Marek', 'Sebastian']
