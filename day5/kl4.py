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

    # __str__
    def __str__(self):
        return f"{self.gatunek}, {self.szybkosc}"


or1 = Ptak("Orzeł", 50)
print(or1)  # <__main__.Ptak object at 0x000001A874D78980>, Orzeł, 50
or1.latam()  # Tu Orzeł Lecę z szybkością: 50 km/h

kur1 = Ptak("Kura", 0)
print(kur1)  # Kura, 0
kur1.latam()  # Tu Kura Lecę z szybkością: 0 km/h
