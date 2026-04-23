# hermetyzacja
class Car:
    """
    Klasa opisujaca samochód w Pythonie
    """

    def __init__(self, model, year):
        """
        Metoda inicjalizująca - konstruktor
        :param model:
        :param year:
        """
        self.model = model
        self.year = year

        # hermetyzacja
        # pole prywatne
        # name mangling
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi: {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10


car = Car("Fiat", 1992)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()

# pole oznaczone jako prywatne - nie da się odczytac
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car.__predkosc)  # 50
# car.licznik()  # Prędkość wynosi: 50 km/h
# car.__predkosc = 0
# print(car.__predkosc)  # 50
# car.licznik()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()
# Prędkość wynosi: 0 km/h

# enkapsulacja - hermetyzownie pol, dodawanie metod do odczytu i zapisu tych pol (setter, getter)