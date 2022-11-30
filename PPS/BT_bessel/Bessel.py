import numpy as np
from math import *

class Bessel:

    def __init__(self):
        self.arr = []
        self.y = []
        self.a = []
        self.x = []
        self.h = None

    def read_file(self, string):
        f = open(string, 'r')
        while True:
            input_str = f.readline()
            if input_str == '':
                break
            arr = input_str.split(" ")
            self.x.append(float(arr[0]))
            self.y.append(float(arr[1]))
        self.h = self.x[1] - self.x[0]
        f.close()

    def hoocne_multiply(self, arr):
        b = [1, -arr[0]]
        k = 1
        while k < len(arr):
            b.append(0)
            self.a = [b[0]]  # an = bn
            c = arr[k]
            for i in range(1, len(b)):
                a_k = b[i] - b[i - 1] * c  # a_k = b_k - b_(k + 1) * c
                self.a.append(a_k)
            b = self.a.copy()
            k += 1
        else:
            self.a = b.copy()
        return self.a

    def hoocne_divive(self, arr, c):
        b = [arr[0]]
        for i in range(1, len(arr)):
            b_k = arr[i] + b[i - 1] * c  # b_k = a_k + b_k-1 * c
            b.append(float(b_k))
        return b

    def delta_y(self, begin, end):
        k = end - begin
        if k == 1:
            return self.y[end] - self.y[begin]
        return self.delta_y(begin + 1, end) - self.delta_y(begin, end - 1)

    def factorial(self, n):
        if n == 0:
            return 1
        return self.factorial(n - 1) * n

    #S_(2K)
    def bessel_even(self, middle, k):
        begin = middle - k
        end = begin + 2*k
        delta_1 = self.delta_y(begin, end)
        delta_2 = self.delta_y(begin + 1, end + 1)
        delta = (delta_1 + delta_2) / (self.factorial(2*k) * 2)
        temp_u = []
        for i in range(1, k+1):
            temp_u.append(((2*k-1)/2)**2)
        temp_u = self.hoocne_multiply(temp_u)
        temp_u = [temp_u[j] * delta for j in range(len(temp_u))]

        u = []
        for i in range(len(temp_u)-1):
            u.append(temp_u[i])
            u.append(0.0)
        u.append(temp_u[-1])
        return u

    #S_(2k+1)
    def bessel_odd(self, middle, k):
        begin = middle - k - 1
        end = begin + (2*k + 1)
        delta = self.delta_y(begin, end) / self.factorial(2*k+1)
        temp_u = []
        for i in range(1, k+1):
            temp_u.append(i**2)
        temp_u = self.hoocne_multiply(temp_u)
        temp_u = [temp_u[j] * delta for j in range(len(temp_u))]

        u = []
        for i in range(len(temp_u)):
            u.append(temp_u[i])
            u.append(0.0)
        return u

    #all
    def bessel(self):
        middle = int(len(self.x) / 2 - 1)
        print(middle)
        y0 = self.y[middle]
        y1 = self.y[middle + 1]
        init_value = self.delta_y(middle, middle + 1)
        p = np.zeros(len(self.x)).tolist()
        p.append(init_value)
        p.append((y0 + y1)/2)
        print('y', p)
        count_even = middle + 1
        count_odd = count_even - 1
        for k in range(1, count_odd):
            b_odd = self.bessel_odd(middle, k)
            for i in range(len(b_odd)):
                p[-i-1] += b_odd[len(b_odd) - i - 1]
            print('odd: ', b_odd)

        for k in range(1, count_even):
            b_even = self.bessel_even(middle, k)
            for i in range(len(b_even)):
                p[-i-1] += b_even[len(b_even) - i - 1]
            print('even: ', b_even)

        print(p)
        print(self.hoocne_divive(p, self.u(3.5, 4, 1)).pop())

    def t(self, x, x0, h):
        return -(x - x0) / h

    def u(self, x, x0, h):
        return self.t(x, x0, h) - 1/2

    def run(self):
        self.read_file("input.txt")
        self.bessel()


if __name__ == '__main__':
    bt = Bessel()
    bt.run()