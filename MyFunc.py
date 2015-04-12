# coding=utf-8
import numpy as np

# Функция для точного решения

def acc_sol(t, x, y):
    return 3 * t * (x + 2 * y) * np.sin(5 * x) + y - x ** 2


# Функция f неоднородности двифференциального уранвнения u'_t = u''_xx + u''_yy + f

def right_part(t, x, y):
    return 3 * (x + 2 * y) * np.sin(5 * x) - 3 * t * (10 * np.cos(5 * x) - 25 * (x + 2 * y) * np.sin(5 * x)) - 2


# Метод прогонки

def progon(a, b, c, d):
    N = len(d) - 1

    alpha = np.zeros(N + 1)
    beta = np.zeros(N + 1)
    alpha[1] = -c[0] / b[0]
    beta[1] = d[0] / b[0]

    x = np.zeros(len(d))

    for i in xrange(1, N):
        alpha[i + 1] = -c[i] / (a[i] * alpha[i] + b[i])
        beta[i + 1] = (d[i] - a[i] * beta[i]) / (a[i] * alpha[i] + b[i])

    x[N] = (d[N] - a[N] * beta[N]) / (b[N] + a[N] * alpha[N])
    for i in reversed(xrange(N)):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]
    return np.array(x)



