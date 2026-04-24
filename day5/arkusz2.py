import pandas as pd

excel_data = pd.read_excel('sales.xlsx')
print(excel_data)
#   Sales Date    Sales Person  Amount
# 0 2018-05-12      Sila Ahmed   60000
# 1 2019-12-06     Mir Hossain   50000
# 2 2020-08-09    Sarmin Jahan   45000
# 3 2021-04-07  Mahmudul Hasan   30000

data = pd.DataFrame(excel_data)
print(data.columns)
print(data.values)
print(data.items())

print(data.index[-1])  # 3
print(data.columns[0])  # Sales Date

print(50 * "-")
print(data['Amount'].median())  # 47500.0

# filtrowanie danych
print(data[data['Amount'] > 46000])
#   Sales Date Sales Person  Amount
# 0 2018-05-12   Sila Ahmed   60000
# 1 2019-12-06  Mir Hossain   50000

dane_filter = data[data['Amount'] > 46000]

# zapis do excela
dane_filter.to_excel('dane.xlsx')
