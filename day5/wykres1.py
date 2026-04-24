import matplotlib.pyplot as plt

# pip install matplotlib
# biblioteka do wykresów

x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 9, 11]

# plt.plot(x, y)
plt.scatter(x, y, c="red")
plt.title("Wykres punktowy")

plt.xlabel("Oś X")
plt.ylabel("Oś Y")

plt.savefig("wykres.png")
plt.show()
