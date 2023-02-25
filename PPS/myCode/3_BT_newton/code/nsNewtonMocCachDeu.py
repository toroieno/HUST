import sys 
sys.path.insert(1, '../../../')
from myCode.CasualFunction import *
import numpy as np


class Newton:

    # region Init
    def __init__(self):
        self.x = []
        self.y = []
        self.h = None
        self.v1 = []  # tỷ sai phân newton tiến
        self.v2 = []  # tỷ sai phân newton lùi
        self.BTH = []  # bảng tỷ hiệu, mảng 2 chiều lưu

    # endregion

    # region Bảng tỷ hiệu
    def tinh_sai_phan(self):
        # khởi tạo bảng tỷ hiệu
        for i in range(len(self.x)):
            row = []
            for j in range(len(self.x)):
                row.append(0)
            self.BTH.append(row)

        # gán giá trị cột đầu tiên của mảng là các giá trị y
        for i in range(len(self.y)):
            self.BTH[i][0] = self.y[i]

        # tính sai phân các cấp
        for col in range(1, len(self.x)):
            for row in range(col, len(self.x)):
                self.BTH[row][col] = (self.BTH[row][col - 1] - self.BTH[row - 1][col - 1])

        print("Bảng sai phân: ")
        print(np.array(self.BTH))

        for col in range(len(self.x)):
            self.v1.append(self.BTH[col][col])
            self.v2.append(self.BTH[len(self.x) - 1][col])

    # endregion

    # region Newton tiến mốc cách đều
    def ns_newton_tien_cach_deu(self):
        p = [self.y[0]]
        for i in range(1, len(self.x)):
            arr_t = [k for k in range(i)]
            w = hoocne_multiply(arr_t)
            p.insert(0, 0)
            for j in range(len(p)):
                w[j] = w[j] * (self.v1[i] / factorial(i))
                p[j] = p[j] + w[j]

        return p

    # endregion

    # region Newton lùi mốc cách đèu
    def ns_newton_lui_cach_deu(self):
        p = [self.y[len(self.x) - 1]]
        for i in range(1, len(self.x)):
            arr_t = [-k for k in range(i)]
            w = hoocne_multiply(arr_t)
            p.insert(0, 0)
            for j in range(len(p)):
                w[j] = w[j] * (self.v2[i] / factorial(i))
                p[j] = p[j] + w[j]

        return p

    # endregion

    # region Main
    def run(self):
        self.x, self.y = read_file('../input.txt')
        self.h = self.x[1] - self.x[0]
        self.tinh_sai_phan()

        # check đầu vào là tăng(newton tiến) hay giảm(newton lùi)
        flag = True if self.x[1] > self.x[0] else False
        p = self.ns_newton_tien_cach_deu() if flag else self.ns_newton_lui_cach_deu()
        if flag:
            print("\nP(x)(ns_tien_cach_deu) = ", p)
        else:
            print("\nP(x)(ns_lui_cach_deu) = ", p)

        # tính giá trị của đa thức tại x = c
        c = float(input('Cần tính tại x = '))
        t_value = t(c, self.x[0], self.h) if flag else t(c, self.x[-1], self.h)

        print("t = ", t_value)
        print("\nP(x = %f) = " % c, hoocne_divide(p, t_value).pop())

    # endregion


if __name__ == "__main__":
    bt = Newton()
    bt.run()
