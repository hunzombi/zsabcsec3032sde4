import matplotlib.pyplot as plt
import random

x = [1, 2, 3, 4, 5, 6]
y = []
for i in range(6):
    y.append(random.randint(1, 10))

plt.plot(x, y)
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("MyFirstPlot")

plt.show()