# generator - generuje dane
import time


def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


def kwadrat2(n):
    for x in range(n):  # od 0 do 4
        yield x ** 2


print(kwadrat2(5))  # <generator object kwadrat2 at 0x000001B219850EE0>

kwa = kwadrat2(5)

print(next(kwa))
print(next(kwa))
print(next(kwa))
# 0
# 1
# 4

print("Zrób cokolwiek")
lista = []
lista.append("123456")
print(lista)

print(next(kwa))  # 9
print(next(kwa))  # 16

# print(next(kwa))  # StopIteration - generator zakońćzył pracę

kwa2 = kwadrat2(5)
kwa3 = kwadrat2(10)

print(next(kwa2))
print(next(kwa2))
print(next(kwa2))

print(next(kwa3))
print(next(kwa3))
print(next(kwa3))

print(next(kwa2))

print(next(kwa3))

print(list(kwa3))  # [16, 25, 36, 49, 64, 81]

for i in kwadrat2(10):
    print(i)
    time.sleep(1) # symulujemy długotrwałe przetwarzenie danych