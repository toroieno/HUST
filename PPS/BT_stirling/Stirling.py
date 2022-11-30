import numpy as np
from math import *

class Stirling:

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
    def stirling_even(self, middle, k):
        begin = middle - k
        end = begin + 2*k
        delta = self.delta_y(begin, end) / self.factorial(2*k)
        temp_t = []
        for i in range(1, k+1):
            temp_t.append((i-1)**2)
        temp_t = self.hoocne_multiply(temp_t)
        temp_t = [temp_t[j] * delta for j in range(len(temp_t))]

        t = []
        for i in range(len(temp_t)-1):
            t.append(temp_t[i])
            t.append(0.0)
        t.append(temp_t[-1])

        return t

    #S_(2k+1)
    def stirling_odd(self, middle, k):
        begin = middle - k - 1
        end = begin + (2*k + 1)
        delta_1 = self.delta_y(begin, end)
        delta_2 = self.delta_y(begin + 1, end + 1)
        delta = (delta_1 + delta_2) / (self.factorial(2*k + 1) * 2)
        temp_t = []
        for i in range(1, k+1):
            temp_t.append(i**2)
        temp_t = self.hoocne_multiply(temp_t)
        temp_t = [temp_t[j] * delta for j in range(len(temp_t))]

        t = []
        for i in range(len(temp_t)):
            t.append(temp_t[i])
            t.append(0.0)

        return t

    #all
    def stirling(self):
        middle = int(len(self.x) / 2)
        print(middle)
        init_value = (self.delta_y(middle - 1, middle) + self.delta_y(middle, middle + 1)) / 2
        p = np.zeros(len(self.x) - 2).tolist()
        p.append(init_value)
        p.append(self.y[middle])
        print('y', p)
        count_even = middle + 1
        count_odd = count_even - 1
        for k in range(1, count_odd):
            s_odd = self.stirling_odd(middle, k)
            for i in range(len(s_odd)):
                p[-i-1] += s_odd[len(s_odd) - i - 1]
        for k in range(1, count_even):
            s_even = self.stirling_even(middle, k)
            for i in range(len(s_even)):
                p[-i-1] += s_even[len(s_even) - i - 1]
            print('even: ', s_even)

        print(self.x[middle])
        print(self.hoocne_divive(p, self.t(5.5, self.x[middle], 1)).pop())

    def t(self, x, x0, h):
        return -(x - x0) / h

    def run(self):
        self.read_file("input.txt")
        self.stirling()


if __name__ == '__main__':
    bt = Stirling()
    bt.run()