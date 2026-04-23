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


cz1 = Human("Radek", 45, 189, "m")
print(cz1.imie)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.plec)
# Radek
# 45
# 189
# m
