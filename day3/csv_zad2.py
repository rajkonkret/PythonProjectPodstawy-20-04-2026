import csv

# filename = "records.csv"
filename = "records_discount.csv"

fields = []
rows = []

with open(filename, "r") as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)  # ;
    print(dialect.quotechar)  # "

    # StopIteration - skonczyły sie dane w iteratorze
    csv_f.seek(0)  # powrót na początek odczytu

    # csvreader = csv.reader(csv_f, delimiter=";")
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x000001F41DE67D60> iterator

    fields = next(csvreader)  # odczyt pierwszego wierszaw pliku csv, usatwienie odczytu na następny

    for row in csvreader:  # odczyt od drugiego wiersza
        rows.append(row)  # row - lista

print("Fields:", fields)
print("Rows:", rows)
# Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['radek', 'coe', '3', '0']]

# Fields: ['sku;exp_date;price']
# Rows: [['1;today;200'], ['2;today;100'], ['3;today;50'], ['4;today;200'], ['5;tomorrow;199.99'], ['6;tomorrow;2100'], ['7;today;1200']]

# Fields: ['sku', 'exp_date', 'price']
# Rows: [['1', 'today', '200'],
# ['2', 'today', '100'],
# ['3', 'today', '50'],
# ['4', 'today', '200'],
# ['5', 'tomorrow', '199.99'],
# ['6', 'tomorrow', '2100'],
# ['7', 'today', '1200']]
