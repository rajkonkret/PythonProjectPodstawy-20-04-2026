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
print(tekst.count("j", 0, 4))# występuje 0  razy, z prawej strony otwarty, 0123 indeksy
