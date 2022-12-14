from math import *


def f(x):
    return x ** 2


def write_optimized_x(n, a, b):
    g = open("input.txt", "w")
    x = []
    for i in range(n):
        temp = 1 / 2 * ((b - a) * cos(((2 * i + 1) * pi) / (2 * (n + 1))) + (b + a))
        x.append(temp)
    for j in x:
        y = f(j)
        g.write(f'{j} {y}\n')
    g.close()


write_optimized_x(6, 2, 5)
