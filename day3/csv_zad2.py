import csv

filename = "records.csv"

fields = []
rows = []

with open(filename, "r") as csv_f:
    csvreader = csv.reader(csv_f)

    print(csvreader)  # <_csv.reader object at 0x000001F41DE67D60> iterator

    fields = next(csvreader)  # odczyt pierwszego wierszaw pliku csv, usatwienie odczytu na następny

    for row in csvreader:  # odczyt od drugiego wiersza
        rows.append(row)  # row - lista

print("Fields:", fields)
print("Rows:", rows)
# Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['radek', 'coe', '3', '0']]
