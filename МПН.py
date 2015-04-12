# coding=utf-8
import MyFunc as fn
import matplotlib.pyplot as plt
import numpy as np
import time

start = time.time()
# Задание сетки по х
x_min = 0.0
x_max = 1.0
nx = 100
hx = (x_max - x_min) / nx
x = np.arange(x_min, x_max, hx)
Nx = len(x) - 1

# Задание сетки по y
y_min = 0.0
y_max = 2.0
ny = 200
hy = (y_max - y_min) / ny
y = np.arange(y_min, y_max, hy)
Ny = len(y) - 1

# Задание сетки по t
t_min = 0.0
t_max = 2.0
m = 100
tau = (t_max - t_min) / m
t = np.arange(t_min, t_max, tau)

# Числа Куранта
c1, c2 = tau / (hx ** 2), tau / (hy ** 2)

# Точное решение(функция, а не массив)
u = fn.acc_sol

# Неоднородность уравнения u'_t = u''_xx + u''_yy + f (тоже функция, а не массив)
f = fn.right_part

# Решение в n момент времени
U = np.zeros((len(x), len(y)))

for i in xrange(0, len(x)):
    for j in xrange(0, len(y)):

        # для нулевого (n = 0) момента времени.
        U[i][j] = u(t[0], x[i], y[j])


# Массив для Решения в n + 1/2  момент времени
U1 = np.zeros((len(x), len(y)))

# Массив для Решения  в n + 1 момент времени
U2 = np.zeros((len(x), len(y)))


for n in range(0, len(t) - 1):

    for j in xrange(1, Ny):
        # коэффициенты в прогоночной системе для (n + 1/2) момента времени
        a = np.array([-c1 / 2 for i in xrange(len(x))])
        a[0] = 0
        a[Nx] = 0

        b = np.array([(c1 + 1) for i in xrange(len(x))])
        b[0] = 1
        b[Nx] = 1

        C = np.array([-c1 / 2 for i in xrange(len(x))])
        C[0] = 0
        C[Nx] = 0

        d = np.zeros(len(x))
        d[0] = 0.5 * (u(t[n + 1], x[0], y[j])  + u(t[n], x[0], y[j])) + 0.5 * (c2 / 2) * (
            u(t[n], x[0], y[j - 1]) - 2 * u(t[n], x[0], y[j]) \
            + u(t[n], x[0], y[j + 1])) - 0.5 * (c2 / 2) * (
            u(t[n + 1], x[0], y[j - 1]) - 2 * u(t[n + 1], x[0], y[j]) + u(t[n + 1], x[0], y[j + 1]))

        d[Nx] = 0.5 * (u(t[n + 1], x[Nx], y[j]) + u(t[n], x[Nx], y[j])) + 0.5 * (c2 / 2) * (
            u(t[n], x[Nx], y[j - 1]) - 2 * u(t[n], x[Nx], y[j]) \
            + u(t[n], x[Nx], y[j + 1])) - 0.5 * (c2 / 2) * (
            u(t[n + 1], x[Nx], y[j - 1]) - 2 * u(t[n + 1], x[Nx], y[j]) + u(t[n + 1], x[Nx], y[j + 1]))

        for i in xrange(1, Nx):
            d[i] = U[i][j] + (c2 / 2) * (U[i][j-1] - 2 * U[i][j] \
                                               + U[i][j+1]) + (tau / 2) * f(t[n] + tau / 2, x[i], y[j])
        # Численное решение в (n + 1/2) момент времени

        arr = fn.progon(a, b, C, d)
        for i in xrange(0, len(x)):
            U1[i][j] = arr[i]


    for i in xrange(1, len(x) - 1):

        # коэффициенты в прогоночной системе для (n + 1) момента времени

        a = np.array([-c2 / 2 for j in xrange(len(y))])
        a[0] = 0
        a[Ny] = 0

        b = np.array([(c2 + 1) for j in xrange(len(y))])
        b[0] = 1
        b[Ny] = 1

        C = np.array([-c2 / 2 for j in xrange(len(y))])
        C[0] = 0
        C[Ny] = 0

        d = np.zeros(len(y))

        d[0] = u(t[n + 1], x[i], y[0])
        d[Ny] = u(t[n + 1], x[i], y[Ny])

        for j in xrange(1, Ny):
            d[j] = U1[i][j] + (tau / 2) * f(t[n] + tau / 2, x[i], y[j]) + (c1 / 2) * (U1[i+1][j] - 2 * U1[i][j] + U1[i - 1][j])

        arr = fn.progon(a, b, C, d)

        for j in xrange(0, len(y)):
            U2[i][j] = arr[j]

    # Значения на границе для решения в (n + 1) момент времени
    for j in xrange(0, len(y)):
        U2[0][j] = u(t[n+1], x[0], y[j])
        U2[Nx][j] = u(t[n+1], x[Nx], y[j])

    U = U2

finish = time.time()
print (finish - start)

plt.contour(x, y, U2.T)
plt.show()
