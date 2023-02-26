from myCode.CasualFunction import *
from math import sqrt


class NewtonCotes:

    # region Initial Variables
    def __init__(self):
        self.x = None
        self.y = None
        self.f = lambda x: 1 / (x ** 2 + 1)
        self.a = 0
        self.b = 3
        self.n = None
        self.eps = 5e-9
        self.option = 1

    # endregion

    # region Newton Cotez
    def newton_cotes(self):
        h = (self.b - self.a) / self.n
        coef = np.ones(self.n + 1)
        coef[1:-1:2] = 4
        coef[2:-1:2] = 2
        integral = (h / 3) * np.sum(coef * self.y)
        if self.option == 2:
            d4f_max = max_fourth_derivative(self.f, self.a, self.b, self.n)
            self.eps = ((self.b - self.a) * h ** 5 / 90) * d4f_max

        return integral, self.eps

    # endregion

    # region Trapezoidal - hinh thang
    def trapezoidal(self):
        h = (self.b - self.a) / self.n
        integral = h * (np.sum(self.y) - 0.5 * (self.y[0] + self.y[self.n]))
        if self.option == 2:
            d2f_max = max_second_derivative(self.f, self.a, self.b, self.n)
            self.eps = ((self.b - self.a) * h ** 2 / 12) * d2f_max
        return integral, self.eps

    # endregion

    # region Simpson
    def simpson(self):
        self.x = np.linspace(self.a, self.b, 2 * self.n + 1)
        self.y = self.f(self.x)
        h = (self.b - self.a) / (2 * self.n)
        coef = np.ones(2 * self.n + 1)
        coef[1:2 * self.n:2] = 4
        coef[2:2 * self.n - 1:2] = 2
        integral = (h / 3) * np.sum(coef * self.y)
        if self.option == 2:
            d4f_max = max_fourth_derivative(self.f, self.a, self.b, self.n)
            self.eps = ((self.b - self.a) * h ** 4 / 180) * d4f_max

        return integral, self.eps

    # endregion
    def simpson_luoi_phu(self):
        print('{0:20}|{1:20}|{2:20}'.format('h', 'integral', 'delta'))
        h = (self.b - self.a) / 2
        self.n = int((self.b - self.a) / (2 * h))
        self.x = np.linspace(self.a, self.b, 2 * self.n + 1)
        self.y = self.f(self.x)
        coef = np.ones(2 * self.n + 1)
        coef[1:2 * self.n:2] = 4
        coef[2:2 * self.n - 1:2] = 2
        integral = (h / 3) * np.sum(coef * self.y)
        print('{0:20}|{1:20}|{2:20}'.format(h, integral, ' '))

        temp_h = h / 2
        self.n = int((self.b - self.a) / (2 * temp_h))
        self.x = np.linspace(self.a, self.b, 2 * self.n + 1)
        self.y = self.f(self.x)
        coef = np.ones(2 * self.n + 1)
        coef[1:2 * self.n:2] = 4
        coef[2:2 * self.n - 1:2] = 2
        temp_integral = (temp_h / 3) * np.sum(coef * self.y)
        delta = abs(integral - temp_integral)/3
        print(self.eps)
        print('{0:20}|{1:20}|{2:20}'.format(temp_h, temp_integral, delta))
        while delta > self.eps:
            integral = temp_integral
            h = temp_h
            temp_h = h / 2
            self.n = int((self.b - self.a) / (2 * temp_h))
            self.x = np.linspace(self.a, self.b, 2 * self.n + 1)
            self.y = self.f(self.x)
            coef = np.ones(2 * self.n + 1)
            coef[1:2 * self.n:2] = 4
            coef[2:2 * self.n - 1:2] = 2
            temp_integral = (temp_h / 3) * np.sum(coef * self.y)
            delta = abs(integral - temp_integral)/3
            print('{0:20}|{1:20}|{2:20}'.format(temp_h, temp_integral, delta))

        return temp_integral
    # region Input
    # Example usage
    def choose_input(self):
        print('1. f, a, b, eps')
        print('2. x, y in file input.txt')
        self.option = int(input('choose option 1 or 2: '))
        # khong can luoi phu - dung cong thuc M2
        if self.option == 1:
            self.n = int(
                sqrt((max_second_derivative(self.f, self.a, self.b) * (self.b - self.a) ** 3)) / (12 * self.eps))
            self.x = np.linspace(self.a, self.b, self.n + 1)
            self.y = self.f(self.x)
        elif self.option == 2:
            self.x, self.y = read_file('../input.txt')
            self.n = len(self.x) - 1
            self.a = self.x[0]
            self.b = self.x[-1]

    # endregion

    # region Main
    def run(self):
        self.choose_input()

        # I_nc, eps_nc = self.newton_cotes()
        # print("Newton-Cotes method: ", I_nc, "+/-", eps_nc)
        #
        # I_trap, eps_trap = self.trapezoidal()
        # print("Trapezoidal rule: ", I_trap, "+/-", eps_trap)
        #
        # I_simpson, eps_simpson = self.simpson()
        # print("Simpson's rule: ", I_simpson, "+/-", eps_simpson)

        self.simpson_luoi_phu()

    # endregion


if __name__ == '__main__':
    bt = NewtonCotes()
    bt.run()
