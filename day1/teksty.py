tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

# wydrukowac dużymi literami
# Return a copy of the string with all the cased characters [4] converted to uppercase
# teksty są niemutowalne
tekst.upper()
print(tekst)  # Witaj Świecie, nie zmienia oryginału
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)  # Witaj Świecie
tekst_upper = tekst.upper()
# tekst = tekst.upper()
print(tekst_upper)

print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie

# Witaj Świecie
# 0123456789.... numerowanie od zera
print(tekst[1])  # i
print(tekst[2])  # t
print(tekst[6])  # Ś

print(tekst.index("Ś"))  # 6
print(tekst.index("e"))  # 9, pierwsze z lewej

print(tekst.count("e"))  # występuje 2 razy
# print(tekst.find("w", 1, 2)) # -1

print(tekst.lower().count("w"))  # 2 razy
# Witaj Świecie
# 0123456789....
print(tekst.count("j", 0, 4))  # występuje 0  razy, z prawej strony otwarty, 0123 indeksy

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunięcie białych znaków, wiodących i kończących spacji
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie'
print(type(encode_s))  # <class 'bytes'>, typ bajtowy
# b - bajty
#  \xc5\x9a - Ś w systemie szesnastkowym
# \x - dane w systemie szesnastkowym

print(encode_s.decode("utf-8"))  # Witaj Świecie

imie = "Radek"
print(len(imie))  # długość tekstu, 5
dane = "Świecie"
print(len(dane)),  # 7

# Mam na imię Radek....
print("Mam na imię " + imie)  # Mam na imię Radek

# f-string, wstrzyknięcie zawartości zmiennej do tekstu {}
tekst_format = f"Mam na imię {imie} i lubię Pythona"
print(tekst_format)  # Mam na imię Radek i lubię Pythona

tekst_format = f"\tMam na imię {imie}\n i lubię Pythona.\b"
print(tekst_format)
# "	Mam na imię Radek
#  i lubię Pythona"
# \t - tab
# \n - nowa linia
# \b - backspace

starszy = "witaj %s!"  # %s - string
print(starszy % imie)  # witaj Radek!

print("witaj {}!".format("Radek"))  # witaj Radek!
print(f"witaj {imie}!")  # witaj Radek!


