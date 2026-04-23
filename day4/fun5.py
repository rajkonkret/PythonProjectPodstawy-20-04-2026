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
        return usd  # zwracamy adres funkcji


kantor_usd = kantor("usd")
kantor_eur = kantor("eur")

kantor_eur()  # Wymieniłem: 0 eur na: 0.0 pln
kantor_eur()  # Wymieniłem: 0 eur na: 0.0 plnł
kantor_eur(1000)  # Wymieniłem: 1000 eur na: 4210.0 pln
kantor_eur(200)  # Wymieniłem: 200 eur na: 842.0 pln

kantor_usd()  # Wymieniłem: 0 usd na: 0.0 pln
kantor_usd()  # Wymieniłem: 0 usd na: 0.0 pln
kantor_usd(50000)  # Wymieniłem: 50000 usd na: 181000.0 pln
kantor_usd(1)  # Wymieniłem: 1 usd na: 3.62 pln

waluta1 = input("Podaj walute:")
wymiana = kantor(waluta1.strip().casefold())
kwota1 = input("Podaj kwote:")
print(wymiana(int(kwota1)))
# Podaj walute:eur
# Otwieram kantor
# Podaj kwote:110000
# Wymieniłem: 110000 eur na: 463100.0 pln
# None
