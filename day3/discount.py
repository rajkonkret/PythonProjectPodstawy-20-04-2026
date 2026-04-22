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

object_data = datetime.now().strptime("22/04/2026", "%d/%m/%Y")
print(object_data)  # 2026-04-22 00:00:00
print(type(object_data))  # <class 'datetime.datetime'>

# s, days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2026-04-23

products = [
    {"sku": 1, "exp_date": today, "price": 200},
    {"sku": 2, "exp_date": today, "price": 100},
    {"sku": 3, "exp_date": today, "price": 50},
    {"sku": 4, "exp_date": today, "price": 200},
    {"sku": 5, "exp_date": tomorrow, "price": 199.99},
    {"sku": 6, "exp_date": tomorrow, "price": 2100},
    {"sku": 7, "exp_date": today, "price": 1200},
]

for p in products:
    # print(p)
    # print(p["exp_date"])

    # if p['exp_date'] == today:
    #     pass

    if p["exp_date"] != today:
        continue  # końćzy biezace wykonanie pętli, pobiera kolejny eleemnt

    p['price'] *= 0.8  # price = price * 0.8

    print(f"""
Price for sku: {p['sku']}
is now: {p['price']:.2f}
""")
