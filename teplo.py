# coding=utf-8
from numpy import cos, sqrt, exp, sin
from matplotlib import mlab
import pylab as plt

# Задание сетки по х
x_min = 0.0
x_max = 1.0
n = 200
h = (x_max - x_min) / n
x = mlab.frange(x_min, x_max, h)
N = len(x) - 1

# Задание сетки по t
t_min = 0.0
t_max = 2.0
m = 600
tau = (t_max - t_min) / m
t = mlab.frange(t_min, t_max, tau)

# точное решение
U = [[x[i] + (t[n] - 1) * sin(4 * x[i]) for i in xrange(len(x))] for n in xrange(len(t))]

# Точное решение в нулевой момент времени
uo = map(lambda z: z - sin(4 * z), x)

# Построение Численного Решения:

# коэффициенты уравнения a, b, c
a = -tau / h ** 2
b = 1 + 2 * (tau / h ** 2)
c = a
f = [map(lambda z: sin(4 * z) * (16 * t[n] - 15), x) for n in xrange(len(t))]

# Коэффициенты при граничных условиях
alpha_l = 0
betta_l = 0


alpha_r = 1
betta_r = [h + h * 4 * (t[n] - 1) * cos(4) for n in xrange(len(t))]

# Массивы для Численного решения "u" и коэффициентов прогонки "X" и "Z"
u = [[0 for i in xrange(len(x))] for n in xrange(len(t))]
X = [[0 for i in xrange(len(x))] for n in xrange(len(t))]
Z = [[0 for i in xrange(len(x))] for n in xrange(len(t))]
u[0] = uo

for n in xrange(len(t)):
    X[n][1] = alpha_l
    Z[n][1] = betta_l


# Окончательное построение численного решения в каждый момент времени:

for n in xrange(len(t) - 1):
    # Нахождение Коэффициентов прогонки (Прямой ход)
    for j in range(1, len(x) - 1):
        X[n + 1][j + 1] = - c / (a * X[n + 1][j] + b)
        Z[n + 1][j + 1] = (tau * f[n + 1][j] + u[n][j] - a * Z[n + 1][j]) / (a * X[n + 1][j] + b)

    # Определение решения на правой границе через N -ые коэффициенты прогонки
    u[n + 1][len(x) - 1] = (alpha_r * Z[n + 1][len(x) - 1] + betta_r[n + 1]) / (1 - alpha_r * X[n + 1][len(x) - 1])

    # Нахождение решения (Обратный ход)
    for j in range(0, len(x) - 1)[::-1]:
        u[n + 1][j] = X[n + 1][j + 1] * u[n + 1][j + 1] + Z[n + 1][j + 1]



# Определение функции для нанесения сетки на график
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

# Построение и вывод графика
for n in xrange(5):
    plt.plot(x, u[n*100])

# нанесение сетки на график
axes.grid()
plt.show()


# построение графиков точного и численного решений в момент времени t = 2:
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

plt.plot(x, u[N], linestyle="-", color="black")
plt.plot(x, U[N], linestyle="-", color="red")
plt.legend(("U[N][j]", "U(x)"))

axes.grid()
plt.show()

# погрешность численного решения в момент времени t = 2:
du = map(lambda z, y: abs(z - y), U[N], u[N])
# вывод максимальной погрешности численного решения в  t = 2:
print(max(du))

# построение графика зависимости погрешности численного решения в t = 2:
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

plt.plot(x, du, linestyle="-", color="black")

axes.grid()
plt.show()















