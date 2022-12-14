import numpy as np
import matplotlib.pyplot as plt
from CasualFunction import *


class Lagrange:

    # region Lagrange
    def __init__(self):
        self.y = []
        self.x = []

    def lagrange(self):
        w = hoocne_multiply(self.x)
        summary = np.zeros(len(w))
        for i in range(len(self.x)):
            temp_arr = hoocne_divide(w, self.x[i])
            y_D_i = self.y[i] / D_i(self.x, i)
            temp_arr = [temp_arr[k] * y_D_i for k in range(len(temp_arr))]
            summary = [summary[j] + temp_arr[j] for j in range(len(temp_arr))]
        summary.pop()
        # summary = [round(summary[i]) for i in range(len(summary))]
        return summary

    # endregion

    # region Draw Graph
    def draw_graph(self):
        # self.x.pop()
        # x = np.array(self.x)
        # y = np.array(self.y)
        #
        # plt.scatter(x, y, color="red")
        x_points = np.linspace(self.x[0], self.x[-1]-1, 1000)
        # print('x', x_points)
        y_coeff = self.lagrange()
        # print('y', y_coeff)
        ypoints = [f_x(y_coeff, xpoint) for xpoint in x_points]
        plt.plot(x_points, ypoints)
        # plt.plot(x_points, self.f_lagrange(y_coeff, x_points))
        # plt.savefig("mygraph.png")
        plt.show()

    # endregion

    # region Main

    def run(self):
        self.x, self.y = read_file("../input.txt")
        # self.read_file("../input.txt")
        # print(self.x)
        # print(self.y)
        print('Hệ số xấp xỉ hàm p(x):', self.lagrange())
        # print(Degf_k(self.lagrange(), 3, 2.7))
        x = float(input('bạn muốn tính tại x = bnhiu: '))
        print(f_x(self.lagrange(), x))
        print(Degf_k(self.lagrange(), 3, 2.7))
        self.draw_graph()

    # endregion


if __name__ == "__main__":
    bt = Lagrange()
    bt.run()

