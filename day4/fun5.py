# stworzyc funkcje kantor
# ma miec dwie funkcje wewnętrzne: eur, usd
# w zależności od parametru zwróci jedną z funkcji
# przekazanie kwoty do funkcji usd, eur

def kantor(waluta):
    print("Otwieram kantor")

    def usd(kwota=0):
        print(f"Wymieniłem: {kwota} usd na: {kwota * 3.62} pln")

    def eur(kwota=0):
        print(f"Wymieniłem: {kwota} eur na: {kwota * 4.21} pln")

    if waluta == "eur":
        return eur
    else:
        return usd
