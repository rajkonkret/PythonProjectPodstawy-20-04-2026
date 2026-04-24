# generator - generuje dane

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
