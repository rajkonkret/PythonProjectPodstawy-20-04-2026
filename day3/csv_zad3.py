import pandas

# pip install pandas

data = pandas.read_csv('records_discount.csv', delimiter=";")
print(data)
#    sku  exp_date    price
# 0    1     today   200.00
# 1    2     today   100.00
# 2    3     today    50.00
# 3    4     today   200.00
# 4    5  tomorrow   199.99
# 5    6  tomorrow  2100.00
# 6    7     today  1200.00

print(data.columns)
# Index(['sku', 'exp_date', 'price'], dtype='str')

print(data.values)
# [[1 'today' 200.0]
#  [2 'today' 100.0]
#  [3 'today' 50.0]
#  [4 'today' 200.0]
#  [5 'tomorrow' 199.99]
#  [6 'tomorrow' 2100.0]
#  [7 'today' 1200.0]]

print(data.items)
# <bound method DataFrame.items of    sku  exp_date    price
# 0    1     today   200.00
# 1    2     today   100.00
# 2    3     today    50.00
# 3    4     today   200.00
# 4    5  tomorrow   199.99
# 5    6  tomorrow  2100.00
# 6    7     today  1200.00>
