from myCode.CasualFunction import *


class ReverseInterpolation:

    def __init__(self):
        self.y = []
        self.x = []
        self.h = None

    # region Nội suy ngược mốc không cách đều

    # nội suy ngược các mốc y_i không đều nhau
    def ns_nguoc_lagrange(self):
        w = hoocne_multiply(self.y)
        # print(w)
        summary = np.zeros(len(w))
        for i in range(len(self.y)):
            temp_arr = hoocne_divide(w, self.y[i])
            y_D_i = self.x[i] / D_i(self.y, i)
            temp_arr = [temp_arr[k] * y_D_i for k in range(len(temp_arr))]
            summary = [summary[j] + temp_arr[j] for j in range(len(temp_arr))]
        summary.pop()
        # summary = [round(summary[i]) for i in range(len(summary))]
        # print(summary)
        return summary

    # endregion

    # region Nội suy ngược mốc cách đều

    def ns_moc_cach_deu(self, y_, eps=10e-4):
        delta_0 = delta_y(self.y, 0, 1)
        t0 = (y_ - self.y[0]) / delta_0
        k = 1  # số lần lặp giới hạn
        t_k = t0
        while k < 100:
            sum_ = 0
            for i in range(2, len(self.x)):
                t = multi_t(t_k, i - 1)
                delta_i = delta_y(self.y, 0, i) / (delta_0 * factorial(i))
                sum_ += delta_i * t
            t_temp = t0 - sum_
            if abs(t_temp - t_k) < eps:
                t_k = t_temp
                break
            t_k = t_temp
            k += 1
        if k >= 100:
            return 'no'
        return self.x[0] + self.h * t_k

    # endregion

    # region Draw graph

    def draw_graph(self):
        x = np.array(self.x)
        y = np.array(self.y)

        plt.scatter(x, y, color='red')
        p = self.ns_nguoc_lagrange()
        ypoints = np.linspace(self.y[0] - 0.5, self.y[-1] + 0.5, 100)
        # print(xpoints)
        xpoints = [f_x(p, ypoint) for ypoint in ypoints]
        plt.plot(xpoints, ypoints)
        # plt.savefig("mygraph.png")
        plt.show()

    # endregion

    # region Run

    def run(self):
        self.x, self.y = read_file("../input.txt")
        self.h = self.x[1] - self.x[0]
        coeff_lagrange = self.ns_nguoc_lagrange()
        print(f_x(coeff_lagrange, 1.35))
        print(self.ns_moc_cach_deu(1.35))
        p = self.ns_nguoc_lagrange()
        print(p)
        print(f_x(p, 19.5))
        # print(np.array(self.y))
        self.draw_graph()
    # endregion


if __name__ == '__main__':
    bt = ReverseInterpolation()
    bt.run()
