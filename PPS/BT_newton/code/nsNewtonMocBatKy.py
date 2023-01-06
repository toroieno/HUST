from CasualFunction import *
import numpy as np


class Newton:

    # region Init
    def __init__(self):
        self.x = []
        self.y = []
        self.v1 = []  # Tỷ sai phân newton tiến
        self.v2 = []  # TỶ sai phân newton lùi
        self.BTH = []  # Bảng tỷ hiệu

    # endregion

    # region Bảng tỷ hệu
    # Bảng tỉ hiệu: mảng 2 chiều lưu tỉ sai phân trên đường chéo chính
    def tinh_ty_hieu(self):
        # khởi tạo 1 mảng f 2 chiều
        for i in range(len(self.x)):
            row = []
            for j in range(len(self.x)):
                row.append(0)
            self.BTH.append(row)

        # gán giá trị cột đầu tiên của mảng là các giá trị y
        for i in range(len(self.y)):
            self.BTH[i][0] = self.y[i]

        # tính các tỷ sai phân
        for col in range(1, len(self.x)):
            for row in range(col, len(self.x)):
                self.BTH[row][col] = (self.BTH[row][col - 1] - self.BTH[row - 1][col - 1]) / (
                        self.x[row] - self.x[row - col])

        print("Bảng tỷ hiệu: ")
        print(np.array(self.BTH))

        """
        @:param v1 - dùng cho newton tiến
        @:param v2 - dùng cho newton lùi
        """
        for col in range(len(self.x)):
            self.v1.append(self.BTH[col][col])
            self.v2.append(self.BTH[len(self.x) - 1][col])

    # endregion

    # region Newton tiến
    def ns_newton_tien(self):
        p = [self.y[0]]
        for i in range(1, len(self.x)):
            arr_x = [self.x[k] for k in range(i)]
            w = hoocne_multiply(arr_x)
            p.insert(0, 0)
            for j in range(len(p)):
                w[j] = self.v1[i] * w[j]
                p[j] = p[j] + w[j]

        return p

    # endregion

    # region Newton lùi
    def ns_newton_lui(self):
        p = [self.y[len(self.x) - 1]]
        for i in range(1, len(self.x)):
            arr_x = [self.x[-k] for k in range(1, i + 1)]
            w = hoocne_multiply(arr_x)
            p.insert(0, 0)
            for j in range(len(p)):
                w[j] = self.v2[i] * w[j]
                p[j] = p[j] + w[j]

        return p

    # endregion

    # region Main
    def run(self):
        self.x, self.y = read_file('../input.txt')
        self.tinh_ty_hieu()

        # check đầu vào là tăng(newton tiến) hay giảm(newton lùi)
        flag = True if self.x[1] > self.x[0] else False
        p = self.ns_newton_tien() if flag else self.ns_newton_lui()
        if flag:
            print("\nP(x)(ns_tien) = ", p)
        else:
            print("\nP(x)(ns_lui) = ", p)

        # tính giá trị của đa thức tại x = c
        # c = float(input('Bạn mún tính đa thức tại c = bnhiu nà: '))
        c = 1.8
        print("\nP(x = %f) = " % c, hoocne_divide(p, c).pop())

    # endregion


if __name__ == "__main__":
    bt = Newton()
    bt.run()
