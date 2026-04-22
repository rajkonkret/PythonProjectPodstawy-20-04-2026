from datetime import date, datetime, timedelta

today = date.today()
print("Dzisiejsza data:", today)  # Dzisiejsza data: 2026-04-22

time = datetime.now()
print(time)  # 2026-04-22 12:36:37.677695

print(type(today))  # <class 'datetime.date'>
print(type(time))  # <class 'datetime.datetime'>

print(today.day)  # 22
print(today.year)  # 2026

# foramtowanie daty
formated_date = datetime.now().strftime("%d/%m/%Y")
print(formated_date) # 22/04/2026
print(type(formated_date)) # <class 'str'>

# 11:16
# 11:16:56
# 11:16 am