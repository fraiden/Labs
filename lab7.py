# coding=utf-8
from numpy import cos, sqrt, exp, sin
from matplotlib import mlab
import pylab as plt


def sh(z):
    return (exp(z) - exp(-z)) / 2.0


def ch(z):
    return (exp(z) + exp(-z)) / 2.0


def ch1(v1, v):
    return (exp(v1 - v) + exp(v - v1)) / 2.0

# Задание сетки по х
x_min = 0.0
x_max = 1.0
n = 20
h = (x_max - x_min) / n
x = mlab.frange(x_min, x_max, h)
N = len(x) - 1

# Задание сетки по t
t_min = 0.0
print("Хотите Задать Время Окончания Расчета (1/0) ?")
a = (input())
if a == 1:
    print("t_max = ")
    t_max = input()
if a == 0:
    t_max = 1.0


print("Хотите Задать Шаг ? (1/0)")
a = (input())
if a == 1:
    print("tau = ")
    tau = input()
    m = (t_max - t_min) / tau
if a == 0:
    m = 20
    tau = (t_max - t_min) / m

t = mlab.frange(t_min, t_max, tau)
C = (tau / h)**2

# Точное решение
U = [ch1(x, t[n]) for n in xrange(len(t))]

# Массив для численного решения
u = [[0 for j in xrange(len(x))] for n in xrange(len(t))]

# 1) - Для граничных и начальных условий с первым порядком точности
u[0] = ch(x)
u[1] = map(lambda y, z: y - tau * z, u[0], sh(x))

# Построение численного решения в каждый момент времени
for n in xrange(1, len(t) - 1):
    for j in xrange(1, len(x) - 1):
        u[n+1][j] = u[n][j] * (2 - C) + (C / 2.0) * (u[n][j+1] + u[n][j-1]) + (tau**2 / 2.0) * ch1(x[j], t[n]) - u[n-1][j]

    # Определение численного решения на границах
    u[n+1][0] = (h * exp(t[n+1]) + u[n+1][1]) / (h + 1)
    u[n+1][N] = (h * (exp(1 - t[n+1]) + 3 * exp(t[n+1] - 1)) - 2 * u[n+1][N-1]) / (2 * (2*h - 1))



# построение графиков численного решения в разные моменты времени:
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

for n in xrange(10):
    plt.plot(x, u[n*2], linestyle="-")

axes.grid()
plt.show()

# 2) - Для граничных и начальных условий со вторым порядком точности

# Задание функции для удобства
g = map(lambda z: 0.5 * (exp(1-z) + 3 * exp(z-1)), t)

u[0] = ch(x)
u[1] = map(lambda y, z, c: y - tau * z + (tau**2 / 4) * (y + c), u[0], sh(x), ch1(x, t[1]))

# Построение численного решения в каждый момент времени
for n in xrange(1, len(t) - 1):
    for j in xrange(1, len(x) - 1):
        u[n+1][j] = u[n][j] * (2 - C) + (C / 2.0) * (u[n][j+1] + u[n][j-1]) + (tau**2 / 2.0) * ch1(x[j], t[n]) - u[n-1][j]

    # Определение численного решения на границах
    u[n+1][0] = (1.0 / (2 * h + 3)) * (4 * u[n+1][1] - u[n+1][2] + 2 * h * exp(t[n+1]))
    u[n+1][N] = (1.0 / (4 * h - 3)) * (u[n+1][N-2] - 4 * u[n+1][N-1] + 2 * h * g[n+1])



# построение графиков численного решения в разные моменты времени:
fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

for n in xrange(10):
    plt.plot(x, u[n*2], linestyle="-")

axes.grid()
plt.show()













