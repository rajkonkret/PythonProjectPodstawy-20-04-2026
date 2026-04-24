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

