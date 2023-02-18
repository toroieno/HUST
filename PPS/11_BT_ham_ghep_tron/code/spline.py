from CasualFunction import *


class Spline:
    # region Initial Variable
    def __init__(self):
        self.p = None
        self.option = None
        self.y = None
        self.x = None

    # endregion

    # region Spline 1
    # S1(x) = a_i(x_i-x) + b_i(x-x_{i-1})
    def spline_1(self):
        A = []  # mảng lưu các chỉ soos
        B = []  # mảng lưu các chỉ số
        for i in range(1, len(self.x)):
            h_i = self.x[i] - self.x[i - 1]
            a_i = self.y[i - 1] / h_i
            b_i = self.y[i] / h_i
            a = -a_i + b_i
            A.append(a)
            b = a_i * self.x[i] - b_i * self.x[i - 1]
            B.append(b)
            print('S1[{0},{1}]={2:.3f}x + {3:.3f}'.format(self.x[i - 1], self.x[i], a, b))

        # for draw graph
        self.p = []
        for i in range(1, len(self.x)):
            p_x = [A[i - 1], B[i - 1]]  # Ax + B
            self.p.append(p_x)

    # endregion

    # region Spline 2
    # S2(x) = a_i(x_i-x)^2 + b_i(x-x_{i-1})^2 + C_i
    def spline_2(self):
        h = [0]
        for i in range(1, len(self.x)):
            h_i = self.x[i] - self.x[i - 1]  # h_i = x_i - x_{i-1}
            h.append(h_i)

        m_0 = (self.y[1] - self.y[0]) / (self.x[1] - self.x[0])
        m = [m_0]
        for i in range(1, len(self.x)):
            m_i = -m[i - 1] + 2 * (self.y[i] - self.y[i - 1]) / h[i]
            m.append(m_i)

        C_i = []
        for i in range(len(self.x)):
            c_i = self.y[i] - m[i] * h[i] / 2
            C_i.append(c_i)

        # S2 = Ax^2 + Bx + C
        A = []
        B = []
        C = []
        for i in range(1, len(self.x)):
            a_i = -m[i - 1] / (2 * h[i])
            b_i = m[i] / (2 * h[i])
            a = a_i + b_i
            b = -(2 * self.x[i] * a_i + 2 * self.x[i - 1] * b_i)
            c = a_i * (self.x[i] ** 2) + b_i * (self.x[i - 1] ** 2) + C_i[i]
            A.append(a)
            B.append(b)
            C.append(c)
            print('S2[{0},{1}]={2:.3f}x^2 + {3:.3f}x + {4:.3f}'.format(self.x[i - 1], self.x[i], a, b, c))

        # for draw graph
        self.p = []
        for i in range(1, len(self.x)):
            p_x = [A[i - 1], B[i - 1], C[i - 1]]
            self.p.append(p_x)

    # endregion

    # region Spline 3
    # S3(x) = A
    def spline_3(self):
        h = [0]
        h.extend(np.diff(self.x))
        print('h:', h)
        n = len(self.x)-1

        dh_0 = (self.y[1] - self.y[0]) / (self.x[1] - self.x[0])
        dh_n = (self.y[n] - self.y[n-1]) / (self.x[n] - self.x[n-1])

        d = np.empty(n+1)
        print('d:', d)
        d[0] = 6 / h[1] * ((self.y[1] - self.y[0]) / h[1] - dh_0)
        d[n] = 6 / h[n-1] * (dh_n - (self.y[n] - self.y[n-1]) / h[n-1])
        print('d0', d[0])
        print('dn', d[n])
        lamda = np.empty(n+1)
        muy = np.empty(n+1)
        for i in range(1, n):
            lamda[i] = h[i + 1] / (h[i] + h[i + 1])
            muy[i] = h[i] / (h[i] + h[i + 1])
            d[i] = 6 / (h[i] + h[i + 1]) * ((self.y[i + 1] - self.y[i]) / h[i + 1] - (self.y[i] - self.y[i - 1]) / h[i])

        print('lamda', lamda)
        print('muy', muy)
        m = self.truy_duoi(muy, lamda, d, n)
        print('m:', m)
        A = [0]
        B = [0]
        a = [0]
        b = [0]
        for i in range(1, n+1):
            A_i = 1 / h[i] * (self.y[i - 1] - m[i - 1] * (h[i] ** 2) / 6)
            B_i = 1 / h[i] * (self.y[i] - m[i] * (h[i] ** 2) / 6)
            A.append(A_i)
            B.append(B_i)

            a_i = m[i - 1] / (6 * h[i])
            b_i = m[i] / (6 * h[i])
            a.append(a_i)
            b.append(b_i)
            print('S3[{0},{1}]={2}({3}-x)^3+{4}(x-{5})^3+{6}({7}-x)+{8}(x-{9})'.format(self.x[i - 1], self.x[i],
                                                                                       a[i], self.x[i],
                                                                                       b[i], self.x[i - 1],
                                                                                       A[i], self.x[i],
                                                                                       B[i], self.x[i - 1]))

        # for draw graph
        self.p = []
        for i in range(1, len(self.x)):
            hsA = b[i] - a[i]
            hsB = 3 * (a[i]*self.x[i] - b[i]*self.x[i-1])
            hsC = 3*b[i]*(self.x[i-1]**2) - 3*a[i]*(self.x[i]**2) - A[i] + B[i]
            hsD = a[i]*(self.x[i]**3) - b[i]*(self.x[i-1]**3) + A[i]*self.x[i] - B[i]*self.x[i-1]
            p_x = [hsA, hsB, hsC, hsD]
            self.p.append(p_x)


    # endregion

    def truy_duoi(self, A, B, d, n):
        alpha = np.empty(n + 1)
        beta = np.empty(n + 1)

        C_i = -2
        alpha[1] = B[0] / C_i
        beta[1] = -d[0] / C_i

        for i in range(1, n):
            alpha[i + 1] = B[i] / (C_i - alpha[i] * A[i])
            beta[i + 1] = (A[i] * beta[i] + d[i]) / (C_i - alpha[i] * A[i])

        x = np.empty(n + 1)
        x[n] = (A[n] * beta[n] + d[n]) / (C_i - A[n] * alpha[n])
        for i in range(n - 1, -1, -1):
            x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]

        return x

    # region Choose Option
    def choose_option(self):
        while True:
            print('1. spline 1 - S1 = Ax + B')
            print('2. spline 2 - S2 = Ax^2 + Bx + C')
            print('3. spline 3 - S3 = Ax^3 + Bx^2 + Cx + D')
            self.option = int(input('choose 1 option: '))
            if self.option == 1:
                self.spline_1()
            elif self.option == 2:
                self.spline_2()
            elif self.option == 3:
                self.spline_3()
            else:
                print('end.')
                break
            self.draw_graph()

    # endregion

    # region Draw Graph
    def draw_graph(self):
        x = np.array(self.x)
        y = np.array(self.y)
        plt.scatter(x, y, color="red")

        # draw graph
        for i in range(1, len(self.x)):
            x_points = np.linspace(self.x[i - 1], self.x[i], 1000)
            y_points = [f_x(self.p[i - 1], x_point) for x_point in x_points]
            plt.plot(x_points, y_points)

        # plt.savefig("mygraph.png")
        plt.show()

    # endregion

    # region Main
    def run(self):
        self.x, self.y = read_file('../input.txt')
        self.spline_3()
        self.draw_graph()
        # self.choose_option()

    # endregion


# ------------------------------------------------
if __name__ == '__main__':
    bt = Spline()
    bt.run()
