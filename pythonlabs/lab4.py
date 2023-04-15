import numpy as np
import matplotlib.pyplot as plt

try:
    with open("data.txt", "r") as f:
        data = np.loadtxt(f)
        x_values = data[:, 0]
        y_values = data[:, 1]
        print("Данные загружены ")
except FileNotFoundError:
    print("Файл не найден. Ручной режим.")
    x_min = float(input("Введите минимальное значение x: "))
    x_max = float(input("Введите максимальное значение x: "))
    step = float(input("Введите шаг вычисления: "))

    def f(x, a, b, c):
        return a * np.sin(b * x) + c

    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    c = float(input("Введите значение c: "))

    x_values = np.arange(x_min, x_max + step, step)

    y_values = f(x_values, a, b, c)

    with open("data.txt", "w") as f:
        for i in range(len(x_values)):
            f.write("{:.3f}\t{:.3f}\n".format(x_values[i], y_values[i]))
        print("Данные сохранены в файл data.txt")

fig, ax = plt.subplots()

ax.plot(x_values, y_values)

ax.set_title("График Функции")
ax.set_xlabel("X")
ax.set_ylabel("Y")

plt.show()

fig.savefig("graph.svg")
