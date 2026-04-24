import time
from itertools import zip_longest

imiona = ["Radek", "Tomek", "Agata", "Marek", 'Asia']
wiek = [44, 56, 23, 38]

zipped = zip_longest(imiona, wiek, fillvalue=None)
print(zipped)  # <itertools.zip_longest object at 0x000001BE8E6DE930>

# for item in zipped:
#     print(item)
# ('Radek', 44)
# ('Tomek', 56)
# ('Agata', 23)
# ('Marek', 38)
# ('Asia', None)

print(40 * "-")
lista = []
for o, w in zipped:
    print(o, w)
    time.sleep(1)
    lista.append(o)
# ----------------------------------------
# ----------------------------------------
# Radek 44
# Tomek 56
# Agata 23
# Marek 38
# Asia None

print(lista)  # ['Radek', 'Tomek', 'Agata', 'Marek', 'Asia']
