# wyjątki - błędy podczas wykonywania programy

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\PythonProjectPodstawy-20-04-2026\day2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1
print("Dalej...")

try:
    # print(5 / 0)
    # int("A")
    # print("A" * "23")
    # raise KeyError  # rzucenie wyjątku
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except ValueError:
    print("Bład wartości")
except TypeError:
    print("Bład typu")
except Exception as e:
    print("Bład:", e)
else:  # wykona się tylko gdy nie ma błedu
    print("Wynik:", wynik)
finally:  # wykona się zawsze
    print("Kolejne obliczenia")

print("Dalej...")
# try except - [else - finally]
