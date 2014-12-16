# coding=utf-8
__author__ = 'maxim'

from math import log
from math import cos
from math import sin
from matplotlib import mlab
import pylab as plt

e1, e2, e3 = 10 ** (-3), 10 ** (-6), 10 ** (-9)

x_min = 0.0
x_max = 10.0
n = 200
h = (x_max - x_min) / n
x = mlab.frange(x_min, x_max, h)
x1 = list(x)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)

def f(z):
    return log(z ** 2 + 3 * z + 1) - cos(2 * z - 1)

y = map(lambda z: log(z ** 2 + 3 * z + 1) - cos(2 * z - 1), x)

def u(z):
    return (2 * z + 3) / (z ** 2 + 3 * z + 1) + 2 * sin(2 * z - 1)

# М Е Т О Д   Н Ь Ю Т О Н А

F = open('Ecuations.txt', 'w')
F.write('Метод Ньютона' + '\n')

X = [1.0]
X.append(X[0] - f(X[0]) / u(X[0]))
i = 1
while abs(X[i] - X[i - 1]) > e3:
    F.write(str(X[i]) + '\n')
    X.append(X[i] - f(X[i]) / u(X[i]))
    i += 1
F.write(str(X[i]) + '\n')

F.close()

print "Метод Ньютона"
print "кол-во итераций = ", i
print "Ошибка = ", abs(X[i] - X[i - 1])
print "Значение корня = ", X[i]


# М Е Т О Д   Д И Х О Т О М И И

F = open('Ecuations.txt', 'a')
F.write('Метод Дихотомии' + '\n')
a, b = x[0], x[x1.index(1)]
root = 0
i1 = 0
while abs(a - b) > e3:

    c = (a + b) / 2
    if f(c) * f(a) < 0:
        b = c
    elif f(b) * f(c) < 0:
        a = c
    root = c
    F.write(str(root) + '\n')
    i1 += 1

F.close()
print "Метод Дихотомии"
print "Кол-во итераций", i1
print "Ошибка = ", abs(a - b)
print "Значение корня = ", root

F = open('Ecuations.txt', 'a')
F.write(str(abs(root - X[i])) + '\n')
F.close()

plt.plot(x, y)
axes.grid()
plt.show()
