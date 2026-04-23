def all_params(a, b, /, c=42, d=256):
    print(f'{a=}, {b=}')
    print(f'{c=}, {d=}')


all_params(1, 2)
all_params(1, 2, 3)
all_params(1, 2, 3, 4)

all_params(1, 2, c=8)
all_params(1, 2, c=8, d=90)


# / oddziela parametry po nazwie od parametrów pozycyjnych
# a,b - muszą byc przekazywane po pozycji !!!
# TypeError: all_params() got some positional-only arguments passed as keyword arguments: 'a, b'
# all_params(a=1, b=2, c=89, d=98)

def all_params2(name, b, /, c=42, *args, d=67, **kwargs):
    print(f"{name=}")
    print(f"{b=}, {c=}, {d=}")
    print(f"{args=}")
    print(f"{kwargs=}")


all_params2("Radek", 2)
all_params2("Radek", 2, 3)
all_params2("Radek", 2, c=3)
all_params2("Radek", 2, 3, 4, 5, 6, 7, 8, 9)
all_params2("Radek", 2, 3, 4, 5, 6, 7, 8, 9, d=90)
all_params2("Radek", 2, 3, d=90)
all_params2("Radek", 2, 3, 4, 5, 6, 7, 8, 9, d=90, e=90, g=90, h=890)
# name='Radek'
# b=2, c=3, d=90
# args=(4, 5, 6, 7, 8, 9)
# kwargs={'e': 90, 'g': 90, 'h': 890}

all_params2("Radek", 2, 3, 4, 5, 6, 7, 8, 9, d=90, e=90, g=90, name=890)
# name='Radek'
# b=2, c=3, d=90
# args=(4, 5, 6, 7, 8, 9)
# kwargs={'e': 90, 'g': 90, 'name': 890} -> kwargs['name']
