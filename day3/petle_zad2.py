dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}

# wypisze klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)
# imie
# nazwisko

# wypisanie wartosci
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wypisze pary
for i in dictionary.items():
    print(i)

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski

# sep
# string inserted between values, default a space.
# end
# string appended after the last value, default a newline.

for k, v in dictionary.items():
    print(k, v, sep="<= = =>")
# imie<= = =>Radek
# nazwisko<= = =>Kowalski

for k, v in dictionary.items():
    print(k, v, sep="<= = =>", end=" | ")
# imie<= = =>Radek | nazwisko<= = =>Kowalski |

print("Radek")  # end="\n"
# imie<= = =>Radek | nazwisko<= = =>Kowalski | Radek

print("następna linijka")  # następna linijka
