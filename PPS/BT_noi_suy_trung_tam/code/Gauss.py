import numpy as np
from math import *

class Gauss:

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

    def gauss_1_t_coeff(self):
        # lấy chỉ số trung tâm của input x
        middle = int(len(self.x) / 2)
        # khởi tạo 2 biến trái phải nhằm chạy về 2 phía
        left = right = middle
        # biến flag dùng để đỏi hướng
        flag_direction = -1
        # x0 là biến trung tâm
        x0 = self.x[middle]
        # p = y0 + delta(y0)*t
        p = [self.delta_y(middle, middle + 1), self.y[middle]]
        # khởi tạo mảng temp và dùng hoocne nhân
        temp_arr = [0]
        # đánh chỉ số dưới của delta
        delta_index = middle
        # số mũ của delta tương ứng với mẫu là k!
        k = 2
        while (left >= 0) and (right < (len(self.x) - 1)):
            if flag_direction == -1:
                # thay đổi chỉ số dưới của delta khi nhảy sang phải
                delta_index -= 1
                right += 1
                # nhân thêm t - 1, t - 2,... t-n
                temp_arr.append(flag_direction * (delta_index - middle))
                temp_t = self.hoocne_multiply(temp_arr)
                # tính giá trị hệ số trước t -> nhân vào với mảng hệ só t ở trên
                temp_delta = self.delta_y(delta_index, delta_index+k) / self.factorial(k)
                temp_t = [temp_t[j] * temp_delta for j in range(len(temp_t))]
                # thêm phần từ 0 vào đầu nhằm mục đích cộng đồn
                p.insert(0, 0)
                p = [p[j] + temp_t[j] for j in range(len(temp_t))]
            else:
                left -= 1
                # nhân thêm t + 1, t + 2,...
                temp_arr.append(flag_direction * (delta_index - middle))
                temp_t = self.hoocne_multiply(temp_arr)
                # tính giá trị hệ số trước t -> nhân vào với mảng hệ só t ở trên
                temp_delta = self.delta_y(delta_index, delta_index + k) / self.factorial(k)
                temp_t = [temp_t[j] * temp_delta for j in range(len(temp_t))]
                # thêm phần từ 0 vào đầu nhằm mục đích cộng đồn
                p.insert(0, 0)
                p = [p[j] + temp_t[j] for j in range(len(temp_t))]

            flag_direction = -flag_direction
            k += 1
        t = self.t(2.5, x0, self.h)
        print(self.hoocne_divive(p, t).pop())
        return p

    def gauss_2_t_coeff(self):
        # lấy chỉ số trung tâm của input x
        middle = int(len(self.x) / 2)
        # khởi tạo 2 biến trái phải nhằm chạy về 2 phía
        left = right = middle
        # biến flag dùng để đỏi hướng
        flag_direction = 1
        # x0 là biến trung tâm
        x0 = self.x[middle]
        # p = y0 + delta(y-1)*t
        p = [self.delta_y(middle - 1, middle), self.y[middle]]
        # khởi tạo mảng temp và dùng hoocne nhân
        temp_arr = [0]
        # đánh chỉ số dưới của delta
        delta_index = middle - 1
        # số mũ của delta tương ứng với mẫu là k!
        k = 2
        while (left >= 0) and (right < (len(self.x) - 1)):
            if flag_direction == -1:
                # thay đổi chỉ số dưới của delta khi nhảy sang phải
                delta_index -= 1
                right += 1
                # nhân thêm t - 1, t - 2,... t-n
                temp_arr.append(flag_direction * (delta_index - middle))
                temp_t = self.hoocne_multiply(temp_arr)
                # tính giá trị hệ số trước t -> nhân vào với mảng hệ só t ở trên
                temp_delta = self.delta_y(delta_index, delta_index+k) / self.factorial(k)
                temp_t = [temp_t[j] * temp_delta for j in range(len(temp_t))]
                # thêm phần từ 0 vào đầu nhằm mục đích cộng đồn
                p.insert(0, 0)
                p = [p[j] + temp_t[j] for j in range(len(temp_t))]
            else:
                left -= 1
                # nhân thêm t + 1, t + 2,...
                temp_arr.append(flag_direction * (delta_index - middle))
                temp_t = self.hoocne_multiply(temp_arr)
                # tính giá trị hệ số trước t -> nhân vào với mảng hệ só t ở trên
                temp_delta = self.delta_y(delta_index, delta_index + k) / self.factorial(k)
                temp_t = [temp_t[j] * temp_delta for j in range(len(temp_t))]
                # thêm phần từ 0 vào đầu nhằm mục đích cộng đồn
                p.insert(0, 0)
                p = [p[j] + temp_t[j] for j in range(len(temp_t))]

            flag_direction = -flag_direction
            k += 1
        t = self.t(2.5, x0, self.h)
        print(self.hoocne_divive(p, t).pop())
        return p

    def t(self, x, x0, h):
        return (x - x0) / h

    def run(self):
        self.read_file("../input.txt")
        # print(self.bt(1, 0.2, 100, 11.75))
        # print(self.newtoncachdeu_x_solve(2.5))
        print(self.gauss_2_t_coeff())
        # print(self.delta_y(1, 3))
        # print(self.newtonbatky())
        # print(self.hoocne_divive(self.newtonbatky(), 13.5).pop())


if __name__ == '__main__':
    bt = Gauss()
    bt.run()