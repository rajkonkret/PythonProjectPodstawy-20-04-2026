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
print(formated_date)  # 22/04/2026
print(type(formated_date))  # <class 'str'>

# 11:16
# 11:16:56
# 11:16 am
formated_time = datetime.now().strftime("%H:%M:%S")
print(formated_time)  # 12:45:30
print(type(formated_time))  # <class 'str'>

formated_time_12h = datetime.now().strftime("%I:%M:%S %p")
print(formated_time_12h)  # 12:46:22 PM
print(type(formated_time_12h))  # <class 'str'>
