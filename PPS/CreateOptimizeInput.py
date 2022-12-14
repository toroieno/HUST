from math import *
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x ** 2) * exp(0.5 * (x**2)) + cos(x**2) * tan(x) - 5 * exp(x)


def write_optimized_x(n, a, b):
    g = open("input.txt", "w")
    x = []
    for i in range(n):
        temp = (1 / 2) * ((b - a) * cos(((2 * i + 1) * pi) / (2 * (n + 1))) + (b + a))
        x.append(temp)
    x.reverse()
    for j in x:
        y = f(j)
        g.write(f'{j} {y}\n')
    g.close()

def draw_graph():
    x_points = np.linspace(2 - 0.5, 5 + 0.5, 1000)
    # print('x', x_points)
    # print('y', y_coeff)
    ypoints = [f(xpoint) for xpoint in x_points]
    plt.plot(x_points, ypoints)
    # plt.plot(x_points, self.f_lagrange(y_coeff, x_points))
    # plt.savefig("mygraph.png")
    plt.show()

print(f(4.5))
draw_graph()
write_optimized_x(6, 2, 5)
