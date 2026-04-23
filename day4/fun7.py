def connect(**opcje):  # dowolna ilośc argumentów nazwanych (keyword)
    print(opcje)


connect()
connect(a=10)  # {'a': 10}
connect(a=10, b=45, c=78, name="Radek")


# {'a': 10, 'b': 45, 'c': 78, 'name': 'Radek'}

def all_args(*args, **kwargs):
    print(args, kwargs)


all_args()
all_args(1, 2, 3, 4)  # (1, 2, 3, 4) {}
all_args(1, 2, 3, 4, a=10)  # (1, 2, 3, 4) {'a': 10}
all_args(a=10, b=90)  # () {'a': 10, 'b': 90}
# all_args(a=10, 0)  # SyntaxError: positional argument follows keyword argument
