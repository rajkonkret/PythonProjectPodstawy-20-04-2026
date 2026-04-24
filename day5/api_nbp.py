# REST API (Representational State Transfer) to
# elastyczny, bezstanowy styl architektury oprogramowania wykorzystujący protokół HTTP do wymiany danych między systemami.
# https://github.com/public-apis/public-apis

# klient http
import requests

# pip install requests

# url = 'https://api.nbp.pl/api/exchangerates/rates/A/USD/'
url = 'https://api.nbp.pl/api/exchangerates/rates/A/CHF/'

response = requests.get(url)
print(response)  # <Response [200]>
# https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP

# 2xx ok
# 3xx - warningi, przekierowania
# 4xx - 404 - brak strony, 400 Bad request
# 5xx - błędy po stronie serwera

print(response.text)

data = response.json()
print(type(data))  # <class 'dict'>
print(data)
# {'table': 'A',
# 'currency': 'dolar amerykański',
# 'code': 'USD',
# 'rates': [{'no': '079/A/NBP/2026', 'effectiveDate': '2026-04-24', 'mid': 3.6294}]}

for i in data:
    print(i)
# table
# currency
# code
# rates

# waluta, code

print("Waluta:", data['currency'])
print("Kod:", data['code'])
# Waluta: dolar amerykański
# Kod: USD

# kurs waluty -> mid
print(data['rates'])
# [{'no': '079/A/NBP/2026', 'effectiveDate': '2026-04-24', 'mid': 3.6294}]
print(data['rates'][0])
# {'no': '079/A/NBP/2026', 'effectiveDate': '2026-04-24', 'mid': 3.6294}
print("Kurs dnia:", data['rates'][0]['mid'])  # Kurs dnia: 3.6294
