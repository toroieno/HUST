from math import *


def g(x):
    # return 3 * x**3 + 2 * x**2 - 3*x + 3
    # return 2 * x**2 - 3*x + 3
    return 2 + 1 * cos(x) + 2 * sin(x) + 3 * cos(2*x) + 4 * sin(2*x)
    # return 5 * pow(x, 4)
    # return 5 * exp(x * 4)
    # return sin(x)
    # return x**2
    # return 1 / (1 + x**2)
    # return 2 * x


def write_file(a, b, kc):
    try:
        f = open('input.txt', 'w')
        k = a
        while k < b:
            x = radians(k)
            y = g(x)
            f.write("{} {}\n".format(k, y))
            k = k + kc
        # for i in range(a, b):
        #   y = g(i)
        #   f.write("{} {}\n".format(i, y))
    except:
        print('read file error!')
    finally:
        f.close()


if __name__ == '__main__':
    write_file(30, 210, 30)
