from myCode.CasualFunction import *
from math import *


class LeastSquare:

    # region Initial Variables
    def __init__(self):
        self.eps = None
        self.b = None
        self.a = None
        self.m = None
        self.Y = None
        self.X = None
        self.n = None
        self.option = 1
        self.y = None
        self.x = None

    # endregion

    # region Input
    def input(self):
        self.x, self.y = read_file('../input.txt')
        self.n = len(self.x)

    # endregion

    # region Some Method
    def arr_pow(self, arr, n):
        temp_arr = arr.copy()
        for each in range(len(temp_arr)):
            temp_arr[each] = temp_arr[each] ** n
        return temp_arr

    def sum_pow(self, arr, n):
        sum_s = 0
        temp_arr = self.arr_pow(arr, n)
        for each in temp_arr:
            sum_s += each

        return sum_s

    def sum_multi(self, arr1, arr2):
        sum_m = 0
        for i in range(len(arr1)):
            sum_m += arr1[i] * arr2[i]

        return sum_m

    def arr_cos(self, r):
        return [cos(r * x) for x in self.x]

    def arr_sin(self, r):
        return [sin(r * x) for x in self.x]

    # gauss-jordan
    def solve_linear_equations(self, A):
        n = len(A)

        # Augment the matrix with a column of zeros
        for i in range(n):
            A[i].append(0)

        # Perform Gauss-Jordan elimination
        for i in range(n):
            pivot = A[i][i]
            if pivot == 0:
                return None  # the system has no unique solution
            for j in range(n):
                if i != j:
                    factor = A[j][i] / pivot
                    for k in range(i, n + 1):
                        A[j][k] -= factor * A[i][k]
            for k in range(n + 1):
                A[i][k] /= pivot

        # Extract the solution from the last column of the matrix
        x = [row[n] for row in A]

        return x
    # endregion

    # region Option
    # region Option 1
    def option_1(self):
        self.m = int(input('m = '))
        temp_a = [self.n]
        for i in range(1, self.m + 1):
            temp_a.append(self.sum_pow(self.x, i))
        temp_a.append(sum(self.y))

        A = [temp_a]
        for i in range(1, self.m + 1):
            temp_a = []
            for j in range(i, self.m + i + 1):
                temp_a.append(self.sum_pow(self.x, j))
            temp_a.append(self.sum_multi(self.arr_pow(self.x, i), self.y))
            A.append(temp_a)

        # print(A)

        x = self.solve_linear_equations(A)
        # print(x)
        # x = x[::-1]
        x.reverse()
        print('P(x)', x)
        y_new = [f_x(x, self.x[i]) for i in range(len(self.x))]
        eps = self.caculate_eps(y_new, self.y)
        # self.a, self.b, self.eps = a, b, eps
        print('sai so: eps = ', eps)
        draw_graph(self.x, x, self.x, self.y)

        return x

    # endregion

    # region Option 2
    def option_2(self):
        self.x = [radians(x) for x in self.x]
        k = int(input('k= '))
        temp_a = [self.n]

        for r in range(1, k + 1):
            sum_cos = sum(self.arr_cos(r))
            sum_sin = sum(self.arr_sin(r))
            temp_a.extend([sum_cos, sum_sin])
        temp_a.append(sum(self.y))

        A = [temp_a]

        for p in range(1, k + 1):
            temp_cos = [sum(self.arr_cos(p))]
            temp_sin = [sum(self.arr_sin(p))]
            for r in range(1, k + 1):
                # tinh dong 2 trong cthuc (6)
                sum_multi_cos = self.sum_multi(self.arr_cos(r), self.arr_cos(p))
                sum_multi_sin = self.sum_multi(self.arr_sin(r), self.arr_cos(p))
                temp_cos.extend([sum_multi_cos, sum_multi_sin])

                # tinh dong 3 trong cthuc (6)
                sum_multi_cos = self.sum_multi(self.arr_cos(r), self.arr_sin(p))
                sum_multi_sin = self.sum_multi(self.arr_sin(r), self.arr_sin(p))
                temp_sin.extend([sum_multi_cos, sum_multi_sin])

            temp_cos.append(self.sum_multi(self.y, self.arr_cos(p)))
            temp_sin.append(self.sum_multi(self.y, self.arr_sin(p)))
            A.extend([temp_cos, temp_sin])

        x = self.solve_linear_equations(A)
        # sai so
        y_new = []

        # print(self.x)
        for x_i in self.x:

            y = x[0]
            j = 1
            for i in range(1, k+1):
                y += x[j]*cos(i*x_i) + x[j+1]*sin(i*x_i)
                j += 2
            y_new.append(y)

        # print(x[0]+x[1]*cos(self.x[0])+x[2]*sin(self.x[0])+x[3]*cos(2*self.x[0])+x[4]*sin(2*self.x[0]))
        # print(y_new)
        eps = self.caculate_eps(y_new, self.y)
        # self.a, self.b, self.eps = a, b, eps
        print('sai so: eps = ', eps)
        print(x)

    # endregion

    # region Option 3
    def option_3(self):
        self.Y = [log10(each) for each in self.y]

        A = [[self.n, sum(self.x), sum(self.Y)], [sum(self.x), self.sum_pow(self.x, 2), self.sum_multi(self.x, self.Y)]]
        # A = [[2, 1, -1, 1], [1, -1, 3, 5], [3, 2, -1, 4]]
        x = self.solve_linear_equations(A)

        a = 10 ** x[0]
        b = x[1] / log10(exp(1))

        print('a = {0} \nb = {1}'.format(a, b))
        y_new = [a * exp(self.x[i] * b) for i in range(len(self.x))]
        eps = self.caculate_eps(y_new, self.y)
        # self.a, self.b, self.eps = a, b, eps
        print('sai so: eps = ', eps)
        return a, b

    # endregion

    # region Option 4
    def option_4(self):
        self.X = [log10(each) for each in self.x]
        self.Y = [log10(each) for each in self.y]

        A = [[self.n, sum(self.X), sum(self.Y)], [sum(self.X), self.sum_pow(self.X, 2), self.sum_multi(self.X, self.Y)]]
        # A = [[2, 1, -1, 1], [1, -1, 3, 5], [3, 2, -1, 4]]
        x = self.solve_linear_equations(A)

        a = 10 ** x[0]
        b = x[1]

        print('a = {0:.5f} \nb = {1:.5f}'.format(a, b))
        y_new = [a*(self.x[i]**b) for i in range(len(self.x))]
        eps = self.caculate_eps(y_new, self.y)
        # self.a, self.b, self.eps = a, b, eps
        print('sai so: eps = ', eps)
        return a, b, eps

    # endregion
    # endregion

    # region Eps
    def caculate_eps(self, arr_new, arr_old):
        sum_square = 0
        for i in range(len(arr_old)):
            sum_square += ((arr_new[i] - arr_old[i]) ** 2)

        return sqrt(1 / len(arr_old) * sum_square)
    # endregion

    # region Chooose_option
    def choose_option(self):
        print('1. y = ax^m + ... + bx + c')
        print('2. y = a + bcosx + csinx')
        print('3. y = ae^(bx)')
        print('4. y = ax^b')
        self.option = int(input('choose option 1 - 4: '))

        if self.option == 1:
            self.option_1()
        elif self.option == 2:
            self.option_2()
        elif self.option == 3:
            self.option_3()
        elif self.option == 4:
            self.option_4()

    # endregion

    # region Main
    def run(self):
        self.input()
        self.choose_option()
    # endregion


if __name__ == '__main__':
    bt = LeastSquare()
    bt.run()
