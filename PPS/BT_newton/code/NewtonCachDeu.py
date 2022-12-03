import numpy as np
from math import *

class Newton:

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

    def tysaiphan(self, begin, end):
        k = end - begin
        return self.delta_y(begin, end) / (self.factorial(k) * (self.h ** k))

    def newtoncachdeu_t_coeff(self):
        # can cai bien self.x[0] bang thang gan gia tri can tinh nhat
        # t = (x - self.x[0]) / self.h
        temp_arr = [0]
        p = [self.y[0]]
        for i in range(1, len(self.x)):
            # he so truoc t
            temp = self.delta_y(0, i) / self.factorial(i)
            # tich cac t(t-1) ... (t - n + 1)
            t_arr = self.hoocne_multiply(temp_arr)
            # nhan he so truoc t voi t(t-1) ... (t - n + 1)
            t_arr = [t_arr[j] * temp for j in range(len(t_arr))]
            # them 0 vao dau nham muc dich cong don
            p.insert(0, 0)
            p = [p[j] + t_arr[j] for j in range(len(p))]
            temp_arr.append(i)
        return p

    def newtoncachdeu_x_solve(self, x):
        t = (x - self.x[0]) / self.h
        return self.hoocne_divive(self.newtoncachdeu_t_coeff(), t).pop()

    def derivate(self, arr, x):
        return self.hoocne_divive(arr, x)[0:-1]

    def f(self, x):
        return x ** 2

    def bt(self, x0, h, n, x):
        i = 1
        distance = abs(x - x0)
        while i < n:
            if x0 < x:
                if (x - x0) <= distance:
                    distance = x - x0
                    i += 1
                    x0 += i*h
                    continue
            break
        self.x = [x0]
        # gia tri y co san chu khong phai goi ham
        self.y = [self.f(x0)]
        while True:
            x0 += h
            if x0 - self.x[0] < 1:
                self.x.append(x0)
                self.y.append(self.f(x0))
            else:
                break
        t = (x - self.x[0]) / h
        # dao ham newton cach deu voi he so theo t -> dung hoocne chia tinh gia tri ham do tai t
        d_newton = self.derivate(self.newtoncachdeu_t_coeff(), t)
        df = self.hoocne_divive(d_newton, t).pop() / h
        return self.newtoncachdeu_x_solve(x), df

    def run(self):
        self.read_file("../input.txt")
        print(self.bt(1, 0.2, 100, 11.75))
        # print(self.newtoncachdeu_x_solve(2.5))
        # print(self.newtoncachdeu_t_coeff())
        # print(self.newtonbatky())
        # print(self.hoocne_divive(self.newtonbatky(), 13.5).pop())


if __name__ == '__main__':
    bt = Newton()
    bt.run()