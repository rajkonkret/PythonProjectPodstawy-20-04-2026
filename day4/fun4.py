# funkcja wewnętrzna , funkcja zagnieżdzona
# uzywana w dekoratorach
def fun1():
    print("To jest fun1")

    def fun2():
        print("to jest fun2")

        def fun3():
            print("To jest fun3")

        return fun3

    # fun2()
    return fun2  # zwraca adres funkcji, referencja


fun1()
xfun = fun1()  # fun1 zwraca adres funkcji fun2
print(xfun)  # <function fun1.<locals>.fun2 at 0x00000243AC2573D0>
print(type(xfun))  # <class 'function'>
xfun()  # to jest fun2
xfun()
xfun()
xfun()
xfun()
xfun()

yfun = xfun()  # fun3 at 0x0000029D31663530>
print(yfun)  # <function fun1.<locals>.fun2.<locals>.fun3 at 0x0000029D31663530>
