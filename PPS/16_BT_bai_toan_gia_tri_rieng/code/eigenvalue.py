import numpy as np

from CasualFunction import *


class Eigenvalue:

    # region Initial Variable
    def __init__(self):
        self.eps = None
        self.u_b = None
        self.u_a = None
        self.n = None
        self.h = None
        self.b = None
        self.a = None
        self.r = None
        self.q = None
        self.p = None

    # endregion

    def eigenvalue(self):
        x = [0]
        x.extend(np.arange(self.a, self.b + self.h, self.h))
        A = np.empty(self.n + 1)
        B = np.empty(self.n + 1)
        C = np.empty(self.n + 1)
        for i in range(1, self.n + 1):
            a_i = self.p(x[i] - self.h / 2)
            a_i_1 = self.p(x[i] + self.h / 2)
            A[i] = - a_i / (self.h**2 * self.r[x[i]])
            B[i] = - a_i_1 / (self.h**2 * self.r[x[i]])
            C[i] = - (a_i + a_i_1 + self.h**2 * self.q[x[i]]) / (self.h ** 2 * self.r[x[i]])
    # region Input
    def input(self):
        self.eps = 10e-6
        self.p = lambda x: 1
        self.q = lambda x: x**2
        self.r = lambda x: 2
        self.a = -1
        self.b = 1
        self.u_a = 0
        self.u_b = 0

        self.n = int((self.b - self.a) / sqrt(self.eps)) + 1
        self.h = (self.b - self.a) / self.n


    # endregion

    # region Main
    def run(self):
        self.input()
        self.eigenvalue()
    # endregion


if __name__ == '__main__':
    bt = Eigenvalue()
    bt.run()
