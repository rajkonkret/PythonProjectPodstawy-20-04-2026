import chardet

# pip install chardet
# Successfully installed chardet-7.4.3
# with open('test.log', "r") as file:
#     lines = file.read()
# print(lines)

# odczyt binarny - rb
with open('test.log', "rb") as fh:
    raw_data = fh.read()

print(raw_data)
# b'Parametr 1\r\nParametr 1\r\nDodane 1\r\nDodane 2\r\nDopisane 2\r\nDo\xc5\x9bdane 2\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'utf-8', 'confidence': 0.833529411764706, 'language': 'pl', 'mime_type': 'text/plain'}
encoding = result['encoding']
print("Kodowanie:", encoding)  # Kodowanie: utf-8

print(50 * "-")
print(raw_data.decode(encoding=encoding))
# --------------------------------------------------
# Parametr 1
# Parametr 1
# Dodane 1
# Dodane 2
# Dopisane 2
# Dośąźćdane 2