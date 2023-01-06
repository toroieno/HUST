from math import *


def g(x):
    # return 2 * x**2 - 3*x + 3
    # return sin(x)
    return x ** 2
    # return 2 * x


def write_file(a, b):
    try:
        f = open('input.txt', 'w')
        i = a
        while i < b:
            y = g(i)
            f.write("{} {}\n".format(i, y))
            i = i + .2


        # for i in range(a, b, 0.2):
        #     y = g(i)
        #     f.write("{} {}\n".format(i, y))
        # f.close()
    except:
        print('read file error!')


if __name__ == '__main__':
    write_file(-1, 1)
