# dekorator
# przyjmuje inną funkcja jako argument
# dodaja, zmienia funkcjonalnosc
# wykorzystuje konstrukcję funkcji wewnętrznej

def dekor(func):
    def wew():
        print("Dodatkowe działanie")
        return func()  # zwracamy wynik dzialania func()

    return wew  # zwracamy adres funkcji wew


@dekor
def hej():
    print("Hej!!")


hej()  # Hej!!
# Dodatkowe działanie
# Hej!!
