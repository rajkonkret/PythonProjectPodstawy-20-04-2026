class Ptak:
    """
    Klasa opsująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Meto inicjalizująca - konstruktor
        :param gatunek:
        :param szybkosc:
        """

        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością:", self.szybkosc, "km/h")

    def wydaj_odglos(self):
        pass

    # __str__
    def __str__(self):
        return f"{self.gatunek}, {self.szybkosc}"


class Kura(Ptak):
    """
    klasa Kura, dziedziczy po klasie Ptak
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # musimy wywołać super(), super() - klasa nadrzędna

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):
        print("ko ko ko ko ko")


# Orzel(Ptak)
class Orzel(Ptak):
    """
    Kalsa Orzel dziedziczy po klasie Ptak
    """

    def wydaj_odglos(self):
        print("Kier kir ki kir")


or1 = Ptak("Orzeł", 50)
print(or1)  # <__main__.Ptak object at 0x000001A874D78980>, Orzeł, 50
or1.latam()  # Tu Orzeł Lecę z szybkością: 50 km/h

kur1 = Ptak("Kura", 0)
print(kur1)  # Kura, 0
kur1.latam()  # Tu Kura Lecę z szybkością: 0 km/h

kur2 = Kura("Kura zielononóżka")
kur2.latam()
kur2.wydaj_odglos()
# Tu Kura Lecę z szybkością: 0 km/h
# Tu Kura zielononóżka Ja nie latam.
# ko ko ko ko ko

or2 = Orzel("Orzeł Bielik", 55)
or2.latam()
or2.wydaj_odglos()
# Tu Orzeł Bielik Lecę z szybkością: 55 km/h
# Kier kir ki kir
