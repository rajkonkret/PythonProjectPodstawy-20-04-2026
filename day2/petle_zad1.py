# pętla - możliwośc wykonnia kodu wielokrotnie
# for - pętla iteracyjna

for i in range(5):  # od 0 do 4
    print(i)

for i in range(20):
    pass  # nic nie rób

print(i)  # 19

for _ in range(15):  # niema zmienna
    print("Test podłoga")
    # print(_) # 14

for i in range(5):
    print(i + 2)
    print(i * 2)

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

lista3 = []
for i in range(10):
    if i % 2 == 0:
        lista3.append(i)

print(lista3)  # [0, 2, 4, 6, 8]

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for i in range(len(lista3)):
    pass

for c in lista3:  # podstawia wszystkie kolejne elemnty z listy
    print(c)

lista_nazwy = ["Ala", "Tomek", 'Zenek', 'Basia']
for p in lista_nazwy:
    print(p)
# Ala
# Tomek
# Zenek
# Basia
