# coding=utf-8
from numpy import cos
from numpy import sqrt
from numpy import exp
from numpy import sin
from numpy import linspace
from matplotlib import mlab
import pylab as plt

# М Е Т О Д   Н Ь Ю Т О Н А

x_min = 0.0
x_max = 1.0
n = 20
h = (x_max - x_min) / n
x = mlab.frange(x_min, x_max, h)

u = [0 for i in range(len(x))]
y = [0 for j in range(len(x))]
uo = map(lambda z: sqrt(z + 1) * sin(z) + exp(-z), x)
u[0], y[0] = 1, 0

for n in range(len(y) - 1):
    y[n + 1] = y[n] + h * ((1 + 2 * x[n]) / (2 * (1 + x[n])) * u[n]
                           + (3 * cos(x[n]) - (3 + 4 * x[n]) * sin(x[n])) / (2 * sqrt(1 + x[n])) - y[n] / 2 * (
        1 + x[n]))
    u[n + 1] = u[n] + y[n] * h

du = map(lambda x, y: abs(x - y), u, uo)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

'''plt.plot(x, du, linestyle="-", marker="^", color="black")
plt.legend(("U(x)", "Uo(x)"))
plt.text(0.25, 1.6, u"Метод Рунге-Кутта", size="22")
axes.grid()
plt.show()'''

# М Е Т О Д   Р У Н Г Е - К У Т Т А;

x_min = 0.0
x_max = 1.0
n = 20
h = (x_max - x_min) / n
x = mlab.frange(x_min, x_max, h)

u = [0 for i in range(len(x))]
y = [0 for j in range(len(x))]
uo = map(lambda z: sqrt(z + 1) * sin(z) + exp(-z), x)
u[0], y[0] = 1, 0


def f(x, y, u):
    return (1 + 2 * x) / (2 * (1 + x)) * u + \
           (3 * cos(x) - (3 + 4 * x) * sin(x)) / \
           (2 * sqrt(1 + x)) - y / (2 * (1 + x))


for i in xrange(len(x) - 1):
    k1 = f(x, y, u)
    q1 = y
    k2 = f(x + h / 2, [y[n] + h / 2 * k1[n] for n in xrange(len(x))], [u[n] + h / 2 * q1[n] for n in xrange(len(x))])
    q2 = [y[n] + h / 2 * k1[n] for n in xrange(len(x))]
    k3 = f(x + h / 2, [y[n] + h / 2 * k2[n] for n in xrange(len(x))], [u[n] + h / 2 * q2[n] for n in xrange(len(x))])
    q3 = [y[n] + h / 2 * k2[n] for n in xrange(len(x))]
    k4 = f(x + h, [y[n] + h * k3[n] for n in xrange(len(x))], [u[n] + h * q3[n] for n in xrange(len(x))])
    q4 = [y[n] + h * k3[n] for n in xrange(len(x))]

    y[i + 1] = y[i] + 1.0 / 6.0 * h * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
    u[i + 1] = u[i] + 1.0 / 6.0 * h * (q1[i] + 2 * q2[i] + 2 * q3[i] + q4[i])
    du = map(lambda x, y: abs(x - y), u, uo)



# Поправка рунге

x_min = 0.0
x_max = 1.0
n = 10
h = (x_max - x_min) / n
x = mlab.frange(x_min, x_max, h)

uo = map(lambda z: sqrt(z + 1) * sin(z) + exp(-z), x)
u1 = [0 for i in range(len(x))]
y1 = [0 for j in range(len(x))]
u1[0], y1[0] = 1, 0


def f(x, y, u):
    return (1 + 2 * x) / (2 * (1 + x)) * u + \
           (3 * cos(x) - (3 + 4 * x) * sin(x)) / \
           (2 * sqrt(1 + x)) - y / (2 * (1 + x))


for i in xrange(len(x) - 1):
    k1 = f(x, y1, u1)
    q1 = y1
    k2 = f(x + h / 2, [y1[n] + h / 2 * k1[n] for n in xrange(len(x))], [u1[n] + h / 2 * q1[n] for n in xrange(len(x))])
    q2 = [y1[n] + h / 2 * k1[n] for n in xrange(len(x))]
    k3 = f(x + h / 2, [y1[n] + h / 2 * k2[n] for n in xrange(len(x))], [u1[n] + h / 2 * q2[n] for n in xrange(len(x))])
    q3 = [y1[n] + h / 2 * k2[n] for n in xrange(len(x))]
    k4 = f(x + h, [y1[n] + h * k3[n] for n in xrange(len(x))], [u1[n] + h * q3[n] for n in xrange(len(x))])
    q4 = [y1[n] + h * k3[n] for n in xrange(len(x))]

    y1[i + 1] = y1[i] + 1.0 / 6.0 * h * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
    u1[i + 1] = u1[i] + 1.0 / 6.0 * h * (q1[i] + 2 * q2[i] + 2 * q3[i] + q4[i])

du1 = map(lambda z, l: abs(z - l), u1, uo)


u2 = [0 for i in range(len(x))]

for i in xrange(len(x)):
    u2[i] = u[i*2] + (u[i*2] - u1[i]) / 15.0

du2 = map(lambda l, k: abs(l - k), u2, uo)

plt.plot(x, du2)
# plt.plot(x, du1)
plt.show()

'''plt.plot(x, du, linestyle="-", marker="^", color="black")
plt.legend(("U(x)", "Uo(x)"))
plt.text(0.25, 12 * 10**(-7), u"Метод Рунге-Кутта", size="22")
plt.text(0.15, 10 * 10**(-7), u"Погрешность. Шаг h = 0.1", size="22")
axes.grid()
plt.show()'''

# М Е Т О Д   А Д А М С А

x_min = 0.0
x_max = 1.0
n = 20
h = (x_max - x_min) / n
x = mlab.frange(x_min, x_max, h)

U = [0 for i in range(len(x))]
v = [0 for j in range(len(x))]
uo = map(lambda z: sqrt(z + 1) * sin(z) + exp(-z), x)
U[0], v[0] = 1, 0



# определеяю посчитанные методом Рунге - Кутта первую и вторую точки для u и u'.

U[1], U[2] = u[1], u[2]
v[1], v[2] = y[1], y[2]

for n in xrange(2, len(x) - 1):
    g = f(x, v, u)
    v[n + 1] = v[n] + h * (23.0 / 12.0 * g[n] - 16.0 / 12.0 * g[n - 1] + 5.0 / 12.0 * g[n - 2])
    U[n + 1] = U[n] + h * (23.0 / 12.0 * v[n] - 16.0 / 12.0 * v[n - 1] + 5.0 / 12.0 * v[n - 2])

dU = map(lambda x, y: abs(x - y), U, uo)

'''plt.plot(x, du, linestyle="-", marker="o", color="black")
plt.text(0.1, 7 * 10 ** (-8), u"график погрешности численного решения, полученного методом адамса", size="15")
plt.legend(("U(x)", "Uo(x)"))
axes.grid()
plt.show()'''
