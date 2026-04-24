# klasa - przepis, szablon
# cechy (zmienne)
# metody - funkcja w klasie
# obiekt - instancja klasy
# klasa musi zostac najpierw zadeklarowana
# tworzenie obiektu uruchamia metodę inicjalizującą (konstruktor) __init__
# __del__ - destruktor
# paradygmaty -> hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# PascalCase, UpperCamelCase
class Human:
    # pass
    """
    Klasa Human opisująca człowieka w Pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    # self - obiekt
    def powitanie(self):
        print(f"Nazywam się: {self.imie}")
        # print(f"Nazywam się: {cz1.imie}") podstawia obiekt klasy

    # napisac metode
    # w zależności plci k - m
    # ruszyłem w drogę
    # ruszyłam w droge
    def ruszaj(self):

        if self.plec == "m":
            print("Ruszył em w drogę")
        else:
            print("Ruszył am w drogę")


# tworzenie obiektu
cz1 = Human()
print(Human.__doc__)  # Klasa Human opisująca człowieka w Pythonie

# print(print.__doc__)
# pydoc - narzędzie do dokumentacji
# cd .\day4\ - wejscie do katalogu day4
# cd .. - wyjscie do wyższego katalogu
# pydoc -b - serwer dokumentacji
# pydoc -w  kl1 - tworzy plik html z dokumentacją

print(cz1)
# <__main__.Human object at 0x0000023757D78980>
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
#
# None
# k

cz1.imie = "Radek"
cz1.wiek = 55
cz1.plec = "m"
print(f"Nazywam się: {cz1.imie}")
print(cz1.imie)  # Radek
print(cz1.wiek)  # 55
print(cz1.plec)  # m

# drugi obiekt innej płci
cz2 = Human()
cz2.imie = "Anna"
cz2.wiek = 45

print(cz2.imie)  # Anna
print(cz2.wiek)  # 45
print(cz2.plec)  # k

cz1.powitanie()
cz2.powitanie()
# Nazywam się: Radek
# Nazywam się: Anna

cz1.ruszaj()
cz2.ruszaj()
# Ruszył em w drogę
# Ruszył am w drogę

# obiekty tej samej klasy
lista = [cz1, cz2]
for i in lista:
    i.ruszaj()
# Ruszył em w drogę
# Ruszył am w drogę
