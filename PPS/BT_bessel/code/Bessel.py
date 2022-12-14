import numpy as np
from CasualFunction import *


class Bessel:

    # region Init
    def __init__(self):
        self.x = []
        self.y = []
        self.x0 = None
        self.h = None

    @staticmethod
    def u(x, x0, h):
        return t(x, x0, h) - 1 / 2

    # endregion

    # region Bessel Even
    # S_(2K)
    def bessel_even(self, middle, k):
        begin = middle - k
        end = begin + 2 * k
        delta_1 = delta_y(self.y, begin, end)
        delta_2 = delta_y(self.y, begin + 1, end + 1)
        delta = (delta_1 + delta_2) / (factorial(2 * k) * 2)
        temp_u = []
        for i in range(1, k + 1):
            temp_u.append(((2 * k - 1) / 2) ** 2)
        temp_u = hoocne_multiply(temp_u)
        temp_u = [temp_u[j] * delta for j in range(len(temp_u))]

        u = []
        for i in range(len(temp_u) - 1):
            u.append(temp_u[i])
            u.append(0.0)
        u.append(temp_u[-1])
        return u

    # endregion

    # region Bessel Odd

    # S_(2k+1)
    def bessel_odd(self, middle, k):
        begin = middle - k - 1
        end = begin + (2 * k + 1)
        delta = delta_y(self.y, begin, end) / factorial(2 * k + 1)
        temp_u = []
        for i in range(1, k + 1):
            temp_u.append(i ** 2)
        temp_u = hoocne_multiply(temp_u)
        temp_u = [temp_u[j] * delta for j in range(len(temp_u))]

        u = []
        for i in range(len(temp_u)):
            u.append(temp_u[i])
            u.append(0.0)
        return u

    # endregion

    # region Main

    # all
    def bessel(self):
        middle = int(len(self.x) / 2 - 1)
        y0 = self.y[middle]
        y1 = self.y[middle + 1]
        init_value = delta_y(self.y, middle, middle + 1)
        p = np.zeros(len(self.x)).tolist()
        p.append(init_value)
        p.append((y0 + y1) / 2)
        count_even = middle + 1
        count_odd = count_even - 1
        for k in range(1, count_odd):
            b_odd = self.bessel_odd(middle, k)
            for i in range(len(b_odd)):
                p[-i - 1] += b_odd[len(b_odd) - i - 1]
            print('odd: ', b_odd)

        for k in range(1, count_even):
            b_even = self.bessel_even(middle, k)
            for i in range(len(b_even)):
                p[-i - 1] += b_even[len(b_even) - i - 1]
            print('even: ', b_even)

        return p

    def run(self):
        self.x, self.y = read_file("../input.txt")
        self.h = self.x[1] - self.x[0]
        self.x0 = self.x[int(len(self.x) / 2) - 1]
        print(f_x(self.bessel(), self.u(3, self.x0, self.h)))

    # endregion


if __name__ == '__main__':
    bt = Bessel()
    bt.run()
