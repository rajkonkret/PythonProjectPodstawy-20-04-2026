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
from colorama import init, Fore, Style

# pip install colorama

init(autoreset=True)


def color_dekorator(fun):
    def wrapper():
        result = fun()
        return Fore.RED + result + Style.RESET_ALL

    return wrapper


@color_dekorator
def napis():
    return "HELLO WORLD!"


print(napis())
