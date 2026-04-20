user = "Tomek"  # str
wiek = 39  # int

wersja = 3.90001
print(type(wersja))  # <class 'float'>, liczba zmiennoprzecinkowa
liczba = 7891234567654321890  # int

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# Witaj Tomek, masz teraz 39 lat.
# %s - string
# %d - digit - liczba

# print("Witaj %d, masz teraz %s lat." % (user, wiek))
# TypeError: %d format: a real number is required, not str

# Witaj Tomek, masz teraz 39 lat.
print(f"Witaj {user}, masz teraz {wiek} lat.")
# Witaj Tomek, masz teraz 39 lat.

# %i - int
# %f - float

print("Używamy wersji Pythona %i" % 3)  # Używamy wersji Pythona 3
print("Używamy wersji Pythona %f" % 3)  # Używamy wersji Pythona 3.000000
print("Używamy wersji Pythona %.2f" % 3.9)  # Używamy wersji Pythona 3.90
print("Używamy wersji Pythona %.1f" % 3.9)  # Używamy wersji Pythona 3.9
print("Używamy wersji Pythona %.0f" % 3.9)  # Używamy wersji Pythona 4 zaorągla
print("Używamy wersji Pythona %.0f" % 3.5)  # Używamy wersji Pythona 4 zaorągla
print("Używamy wersji Pythona %.f" % 3.5)  # Używamy wersji Pythona 4 zaorągla

x = 3.8769
print(x)  # 3.8769
y = round(x)
print(y)  # 4

z = round(x, 2)  # 2 - liczba miejsc po przecinku
print(f"{z=}")  # z=3.88
print(type(z))  # <class 'float'>

print(f"Używamy wersji Pythona {wersja}")  # Używamy wersji Pythona 3.90001
print(f"Używamy wersji Pythona {wersja:.2f}")  # Używamy wersji Pythona 3.90
print(f"Używamy wersji Pythona {wersja:.1f}")  # Używamy wersji Pythona 3.9
print(f"Używamy wersji Pythona {wersja:.0f}")  # Używamy wersji Pythona 4

print(f"{user:<10}")  # "Tomek     "
print(f"{user:>15}")  # "          Tomek"
print(f"{user:^20}")  # "       Tomek        "
print(f"{user:.^20}")  # ".......Tomek........"

print(liczba)  # 7891234567654321890
print(f'Nasza duża liczba: {liczba:,}')  # Nasza duża liczba: 7,891,234,567,654,321,890
print(f'Nasza duża liczba: {liczba:_}')  # Nasza duża liczba: 7_891_234_567_654_321_890
print(f'Nasza duża liczba: {liczba:_}'.replace("_", " "))  # Nasza duża liczba: 7 891 234 567 654 321 890
print(f'Nasza duża liczba: {liczba:_}'.replace("_", "."))  # Nasza duża liczba: 7.891.234.567.654.321.890

# liczba = 1500000000000
liczba = 1_500_000_000_000
print(liczba)  # 1500000000000
print(type(liczba))  # <class 'int'>
