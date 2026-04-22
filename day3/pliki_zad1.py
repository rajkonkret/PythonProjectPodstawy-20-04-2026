# działania z plikami
# contex manager
# with - context manager

#
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================

# w - tworzy nowy plik
# gdy plik istnieje zostania nadpisany (skasowany)
with open("test.log", "w", encoding='utf-8') as f:  # pod f dostaniemy ten filehandler
    f.write("Powitanie\n")
    f.write("Jeszcze jedno\n")

# f.write("") # ValueError: I/O operation on closed file.

# x - tworzy nowy plik
# jesli juz istnieje dostaniemy błąd
# FileExistsError: [Errno 17] File exists: 'test.log'
# with open("test.log", "x",  encoding='utf-8') as f:  # pod f dostaniemy ten filehandler
#     f.write("Powitanie\n")
#     f.write("Jeszcze jedno\n")

# skasuje plik i na nowo utworzy
with open("test.log", "w", encoding='utf-8') as f:  # pod f dostaniemy ten filehandler
    f.write("Parametr 1\n")
    f.write("Parametr 1\n")

with open("test.log", "a", encoding='utf-8') as f:  # pod f dostaniemy ten filehandler
    f.write("Dodane 1\n")
    f.write("Dodane 2\n")
    f.write("Dopisane 2\n")
    f.write("Dośdane 2\n")

with open('test.log', "r", encoding='utf-8') as file:
    lines = file.read()  # wczytanie danych z pliku

print(lines)
# Parametr 1
# Parametr 1
# Dodane 1
# Dodane 2
# Dopisane 2
# Dośdane 2
