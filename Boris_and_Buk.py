from matplotlib import mlab
import numpy as np
import pylab as plt
from matplotlib import animation


# Задание сетки по х
x_min = 0.0
x_max = 1.0
n = 100
h = (x_max - x_min) / n
x = np.arange(x_min, x_max, h)
N = len(x) - 1

# Задание сетки по t
t_min = 0.0
t_max = 1.0
m = 200
tau = (t_max - t_min) / m
t = mlab.frange(t_min, t_max, tau)

# Число куррента
e = tau / h

# Точное решение в нулевой момент времени(импульс)
x0 = 0.1
d = 0.09
imp = np.zeros(len(x))
for i in range(len(x)):
    if abs(x[i] - x0) <= d:
        imp[i] = 1.0
    if abs(x[i] - x0) >= d:
        imp[i] = 0.0
    if abs(x[i] - x0) == d:
        imp[i] = 0.5

# Точное решение на левой границе(импуль)
f_imp = np.zeros(len(t))
for i in range(len(t)):
    if abs(x0 + t[i]) <= d:
        f_imp[i] = 1.0
    if abs(x0 + t[i]) > d:
        f_imp[i] = 0.0
    if abs(x0 + t[i]) == d:
        f_imp[i] = 0.5


# Массивы для Численного решения "u" и "u1"(с коррекцией)
u = np.zeros((len(t), len(x)))
u[0] = imp

u1 = np.zeros((len(t), len(x)))
u1[0] = imp

# Построение решение (уже с коррекцией)
for n in range(0, len(t) - 1):
    for j in range(2, len(x) - 2):
            u[n + 1][j] = u1[n][j] - (e / 2) * (u1[n][j + 1] - u1[n][j - 1]) \
                          + ((e ** 2 / 2) + (1.0 / 8.0)) * (u1[n][j + 1] - 2 * u1[n][j] + u1[n][j - 1])

            s1 = np.sign(u[n][j + 1] - u[n][j])
            fc1 = s1 * max(0, min((s1 * (u[n][j] - u[n][j - 1])), (1.0 / 8.0) * abs(u[n][j + 1] - u[n][j]),
                                  s1 * (u[n][j + 2] - u[n][j + 1])))

            s2 = np.sign(u[n][j] - u[n][j - 1])
            fc2 = s2 * max(0, min((s2 * (u[n][j - 1] - u[n][j - 2])), (1.0 / 8.0) * abs(u[n][j] - u[n][j - 1]),
                                  s2 * (u[n][j + 1] - u[n][j])))

            u1[n + 1][j] = u[n][j] + fc2 - fc1


# создание фигуры
fig, ax = plt.subplots()
line, = ax.plot(x, u1[0])


# функция, для рисования графика
def animate(data):
    line.set_ydata(data)
    return line,


# эта функция нужна для очистки "холста" (в документации на английском не очень понятно написано, но вроде так)
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,


def gen_data():
    """этот генератор через каждые interval (в нашем случае interval = 10) миллисекунд
    возвращает u1[n] и передает этот массив в качестве data в функцию animate(data).
    Animate(data) рисует график u1[n]"""
    n = 0
    while n < len(t) - 4:
        n += 1
        yield u1[n]


ax.set_ylim(-2.0, 2.0)

# а это просто построение анимации
ani = animation.FuncAnimation(fig, animate, gen_data, init_func=init, interval=10, blit=True)

plt.show()














