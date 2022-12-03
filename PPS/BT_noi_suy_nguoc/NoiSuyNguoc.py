import matplotlib.pyplot as plt
import numpy as np
from math import *

class ReverseInterpolation:

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
    
    def f_(self, arr, x):
        return self.hoocne_divive(arr, x).pop()

    def D_i(self, i):
        multi = 1
        for k in range(len(self.y)):
            if k != i:
                multi *= (self.y[i] - self.y[k])
        return multi

    #nội suy ngược các mốc y_i không đều nhau
    def ns_nguoc_lagrange(self):
        w = self.hoocne_multiply(self.y)
        # print(w)
        summary = np.zeros(len(w))
        for i in range(len(self.y)):
            temp_arr = self.hoocne_divive(w, self.y[i])
            y_D_i = self.x[i] / self.D_i(i)
            temp_arr = [temp_arr[k] * y_D_i for k in range(len(temp_arr))]
            summary = [summary[j] + temp_arr[j] for j in range(len(temp_arr))]
        summary.pop()
        # summary = [round(summary[i]) for i in range(len(summary))]
        # print(summary)
        return summary

    #tính tích t(t-1)(t-2)...
    def multi_t(self, t, k):
        if k == 0:
            return t
        return self.multi_t(t, k-1) * (t - k)
    #trường hợp các mốc cách đều
    def ns_moc_cach_deu(self, y_):
        delta_0 = self.delta_y(0, 1)
        t0 = (y_ - self.y[0]) / delta_0
        # delta_2 = self.delta_y(0, 2)
        # print(delta_0)
        # print(delta_2)
        # print('t', t0)
        k = 100 # số lần lặp giới hạn
        t_k = t0
        while k > 0:
            sum_ = 0
            for i in range(2, len(self.x)):
                t = self.multi_t(t_k, i-1)
                delta_i = self.delta_y(0, i) / (delta_0 * self.factorial(i))
                sum_ += delta_i * t
            t_temp = t0 - sum_ 
            if abs(t_temp - t_k) < 10e-4:
                t_k = t_temp
                break
            t_k = t_temp
            k -= 1
        if k <= 0:
            return 'no'
        return self.x[0] + self.h * t_k

    def draw_graph(self):
        x = np.array(self.x)
        y = np.array(self.y)

        plt.scatter(x, y)
        p = self.ns_nguoc_lagrange()
        xpoints = np.linspace(self.x[0]-0.5, self.x[len(p) - 1] + 0.5, 100)
        ypoints = [self.f_(p, xpoint) for xpoint in xpoints]
        plt.plot(xpoints, ypoints)
        # plt.savefig("mygraph.png")
        # plt.show()

    def run(self):
        self.read_file("input.txt")
        coeff_lagrange = self.ns_nguoc_lagrange()
        print(self.f_(coeff_lagrange, 2))
        print(self.ns_moc_cach_deu(1.35))
        # self.draw_graph()


if __name__ == '__main__':
    bt = ReverseInterpolation()
    bt.run()