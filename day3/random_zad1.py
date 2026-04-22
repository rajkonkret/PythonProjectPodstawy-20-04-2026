import random

# działania na liczbach losowych

#  """Return random integer in range [a, b], including both end points.
#         """
print(random.randint(1, 100))  # int, od 1 do 100

print(random.randrange(1, 100))  # int, od 1 do 99
print(random.randrange(5))  # od 0 do 4

print(random.random())  # float, od 0 do 0.9999999 ->  0.600380112524912
print(random.random() * 7)  # float, od 0 do 6.9999999 ->  1.5768172948473143

