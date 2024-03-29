from myCode.CasualFunction import *


class Boundary:

    # region Initial Variable
    def __init__(self):
        self.u_b = None
        self.u_a = None
        self.b = None
        self.a = None
        self.q = None
        self.p = None
        self.h = None
        self.f = None
        self.sigma1 = None
        self.sigma2 = None
        self.muy1 = None
        self.muy2 = None
        self.check_boundary = None

    # endregion

    def boundary(self):
        x = [0]
        x.extend(np.arange(self.a, self.b + self.h, self.h))
        print(x)
        n = int((self.b - self.a) / self.h) + 1
        print(n)
        A = np.empty(n + 1)
        B = np.empty(n + 1)
        C = np.empty(n + 1)
        phi_i = [0]
        for i in range(1, n + 1):
            a_i = self.p(x[i] - self.h / 2)
            a_i_1 = self.p(x[i] + self.h / 2)
            d_i = self.q(x[i])
            phi_i.append(self.f(x[i]))
            A[i] = 1 / (self.h ** 2) * a_i
            B[i] = 1 / (self.h ** 2) * a_i_1
            C[i] = (1 / (self.h ** 2)) * (a_i + a_i_1 + self.h ** 2 * d_i)

        # truy duoi
        alpha = np.empty(n + 1)
        beta = np.empty(n + 1)
        y = np.empty(n + 1)
        if self.check_boundary == 1:
            # truy duoi phai
            alpha[1] = 0
            beta[1] = self.u_a
            for i in range(1, n):
                alpha[i+1] = B[i] / (C[i] - alpha[i] * A[i])
                beta[i+1] = (beta[i] * A[i] + phi_i[i]) / (C[i] - alpha[i] * A[i])
            y[n] = self.u_b
            for i in range(n-1, 0, -1):
                y[i] = alpha[i+1] * y[i+1] + beta[i+1]

            return y

        elif self.check_boundary == 3:
            #truy duoi phai
            a_1 = self.p(x[1] - self.h / 2)
            B[0] = a_1 / self.h
            C[0] = (1 / self.h) * (a_1 + self.h ** 2 * self.q[self.a] + self.sigma1 * self.h)
            alpha[1] = B[0] / C[0]
            beta[1] = self.muy1 / C[0]
            for i in range(1, n):
                alpha[i+1] = B[i] / (C[i] - alpha[i] * A[i])
                beta[i+1] = (beta[i] * A[i] + phi_i[i]) / (C[i] - alpha[i] * A[i])
            y[n] = (A[n] * beta[n] + self.muy2) / (C[n] - A[n] * alpha[n])

            for i in range(n-1, 0, -1):
                y[i] = alpha[i+1] * y[i+1] + beta[i+1]
            return y

    # region Input
    def input(self):
        self.check_boundary = 1  # chọn bài toán biên loại 1 hoặc 3
        # cho khoảng để tính - input x0 < x < x_end
        self.p = lambda x: 1 + x*x
        self.q = lambda x: 4*x*x*x - 6*x*x + 2.25*x
        self.f = lambda x: 53*exp(-x*x)*(1.25*x*x-2.75*x-2)
        self.a = 0
        self.b = 3
        self.h = 0.01
        self.u_a = 53
        self.u_b = 53
        # bien loai 3
        self.sigma1 = 0
        self.sigma2 = 0
        self.muy1 = 0
        self.muy2 = 0

    # endregion

    # region Main
    def run(self):
        self.input()
        y = self.boundary()
        x_points = np.linspace(0, 3, 302)
        y_points = y
        plt.plot(x_points, y_points)
        print(len(y))
        plt.show()
        print('y ', y)
    # endregion


if __name__ == '__main__':
    bt = Boundary()
    bt.run()
