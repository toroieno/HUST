import sys 
sys.path.insert(1, '../../')
from CasualFunction import *


class Lagrange:

    # region variables
    def __init__(self):
        self.y = []
        self.x = []

    # endregion

    # region main algorithm
    def lagrange(self):
        # tính tích (x-x0)(x-x1)...
        w = hoocne_multiply(self.x)
        # khởi tạo mảng lưu hệ số = 0
        summary = np.zeros(len(w))
        for i in range(len(self.x)):
            # tính phép chia w_{n+1}(x) / (x-x_i)
            temp_arr = hoocne_divide(w, self.x[i])
            # tính y / D_i
            y_D_i = self.y[i] / D_i(self.x, i)
            # các hệ số của lần lặp thứ i
            temp_arr = [temp_arr[k] * y_D_i for k in range(len(temp_arr))]
            # cộng dồn hệ số tương ứng
            summary = [summary[j] + temp_arr[j] for j in range(len(temp_arr))]
        
        summary.pop()
        return summary

    # endregion

    # region Main
    def run(self):
        self.x, self.y = read_file("../input.txt")
        print('P(x):', self.lagrange())
        x = float(input('Cần tính tại x = '))
        print(f_x(self.lagrange(), x))
        draw_graph(self.x, self.lagrange(), self.x, self.y)

    # endregion

if __name__ == "__main__":
    bt = Lagrange()
    bt.run()

