import sys

wiek = 47  # int
rok = 2026  # int
temp = 36.6  # float

print(wiek + rok)  # 2073
print(wiek - rok)  # -1979
print(wiek * rok)  # 95222
print(wiek / rok)  # 0.02319842053307009 -> float

print(2026 / 47)  # 43.1063829787234
print(2026 // 47)  # 43 - cześć całkowita dzielenia

print(rok % wiek)  # modulo, reszta z dzielenia, 5
print(43 * 47)  # 2021
print(2026 - 2021)  # 5

print(10 % 3)  # 1

print(wiek ** rok)

print(len(str(wiek ** rok)))  # długośc 3388

# print(len(str(wiek ** rok ** 2))) # długośc 3388
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit
