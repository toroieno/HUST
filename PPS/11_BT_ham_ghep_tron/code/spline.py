from CasualFunction import *


class Spline:
    def __init__(self):
        self.B = None
        self.A = None
        self.y = None
        self.x = None

    # S1(x) = a_i(x_i-x) + b_i(x-x_{i-1})
    def spline_1(self):
        self.A = []  # mảng lưu các chỉ soos
        self.B = []  # mảng lưu các chỉ số
        for i in range(1, len(self.x)):
            h_i = self.x[i] - self.x[i - 1]
            a_i = self.y[i-1] / h_i
            b_i = self.y[i] / h_i
            a = -a_i + b_i
            self.A.append(a)
            b = a_i * self.x[i] - b_i * self.x[i - 1]
            self.B.append(b)
            print('S1[{0},{1}]={2}x + {3}'.format(self.x[i - 1], self.x[i], a, b))

    # S2(x) = a_i(x_i-x)^2 + b_i(x-x_{i-1})^2 + C_i
    def spline_2(self):
        pass

    def spline_3(self):
        pass

    def choose_option(self):
        pass

    def draw_grap(self):
        x = np.array(self.x)
        y = np.array(self.y)
        plt.scatter(x, y, color="red")

        # draw graph
        for i in range(1, len(self.x)):
            x_points = np.linspace(self.x[i - 1], self.x[i], 1000)
            p_x = [self.A[i-1], self.B[i-1]]  # Ax + B Spline1
            y_points = [f_x(p_x, x_point) for x_point in x_points]
            plt.plot(x_points, y_points)

        # plt.savefig("mygraph.png")
        plt.show()

    def run(self):
        self.x, self.y = read_file('../input.txt')
        self.spline_1()
        self.draw_grap()


if __name__ == '__main__':
    bt = Spline()
    bt.run()
