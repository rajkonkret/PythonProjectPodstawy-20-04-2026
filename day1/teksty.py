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

