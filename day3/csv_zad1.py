# csv - dane oddzielone znakiem podziału ,;tab|

# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

import csv

row = ['radek', 'coe', "3", 0]
fields = ['name', 'branch', 'year', 'cgpa']
# radek,coe,3,0

filename = "records.csv"

# newline="" - obejscie problemu pustych linii
with open(filename, "w", newline="") as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

dict_name = dict(zip(fields, row))
print(dict_name)
print(type(dict_name))
# {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': 0}
# <class 'dict'>

filename = "records_dict.csv"

with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()  # zapis nagłówków, nazwy kolumn
    csvwriter.writerow(dict_name)  # dane w słowniku

products = [
    {"sku": 1, "exp_date": 'today', "price": 200},
    {"sku": 2, "exp_date": 'today', "price": 100},
    {"sku": 3, "exp_date": 'today', "price": 50},
    {"sku": 4, "exp_date": 'today', "price": 200},
    {"sku": 5, "exp_date": 'tomorrow', "price": 199.99},
    {"sku": 6, "exp_date": 'tomorrow', "price": 2100},
    {"sku": 7, "exp_date": 'today', "price": 1200},
]

filename = "records_discount.csv"

# list_products = ["sku", "exp_date", "price"]
list_products = [key for key in products[0]]  # wyciąga klucze

with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=list_products, delimiter=";")
    csvwriter.writeheader()  # zapis nagłówków, nazwy kolumn
    csvwriter.writerows(products)  # writerows, podajemy listę słowników
