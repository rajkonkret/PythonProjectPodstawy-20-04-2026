class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    # dopisac metody wypisz_wiek(), wypisz_wzrost()
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")

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


cz1 = Human("Radek", 45, 189, "m")
print(cz1.imie)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.plec)
# Radek
# 45
# 189
# m

cz1.wypisz_wiek()
cz1.wypisz_wzrost()
# Mam 45 lat.
# Mam 189 cm wzrostu.

# obiekt innej płci, przetestowac wszytskie metody na nim
cz2 = Human("Annna", 45, 170)
cz2.wypisz_wzrost()
cz2.wypisz_wiek()
cz2.powitanie()
cz2.ruszaj()
# Mam 170 cm wzrostu.
# Mam 45 lat.
# Nazywam się: Annna
# Ruszył am w drogę
