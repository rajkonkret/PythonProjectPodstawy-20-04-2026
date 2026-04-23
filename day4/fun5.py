# stworzyc funkcje kantor
# ma miec dwie funkcje wewnętrzne: eur, usd
# w zależności od parametru zwróci jedną z funkcji
# przekazanie kwoty do funkcji usd, eur

def kantor(waluta):
    print("Otwieram kantor")

    def usd():
        pass

    def eur():
        pass

    if waluta == "eur":
        return eur
    else:
        return usd
