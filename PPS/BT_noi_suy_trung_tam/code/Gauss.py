from CasualFunction import *


class Gauss:

    # region Init
    def __init__(self):
        self.x = []
        self.y = []
        self.x0 = None
        self.h = None

    # endregion

    # region Gauss I

    def gauss_1_t_coeff(self):
        # lấy chỉ số trung tâm của input x
        middle = int(len(self.x) / 2)
        # khởi tạo 2 biến trái phải nhằm chạy về 2 phía
        left = right = middle
        # biến flag dùng để đỏi hướng
        flag_direction = -1
        # p = y0 + delta(y0)*t
        p = [delta_y(self.y, middle, middle + 1), self.y[middle]]
        # khởi tạo mảng temp và dùng hoocne nhân
        temp_arr = [0]
        # đánh chỉ số dưới của delta
        delta_index = middle
        # số mũ của delta tương ứng với mẫu là k!
        k = 2
        while (left >= 0) and (right < (len(self.x) - 1)):
            if flag_direction == -1:
                # thay đổi chỉ số dưới của delta khi nhảy sang phải
                delta_index -= 1
                right += 1
                # nhân thêm t - 1, t - 2,... t-n
                temp_arr.append(flag_direction * (delta_index - middle))
                temp_t = hoocne_multiply(temp_arr)
                # tính giá trị hệ số trước t -> nhân vào với mảng hệ só t ở trên
                temp_delta = delta_y(self.y, delta_index, delta_index + k) / factorial(k)
                temp_t = [temp_t[j] * temp_delta for j in range(len(temp_t))]
                # thêm phần từ 0 vào đầu nhằm mục đích cộng đồn
                p.insert(0, 0)
                p = [p[j] + temp_t[j] for j in range(len(temp_t))]
            else:
                left -= 1
                # nhân thêm t + 1, t + 2,...
                temp_arr.append(flag_direction * (delta_index - middle))
                temp_t = hoocne_multiply(temp_arr)
                # tính giá trị hệ số trước t -> nhân vào với mảng hệ só t ở trên
                temp_delta = delta_y(self.y, delta_index, delta_index + k) / factorial(k)
                temp_t = [temp_t[j] * temp_delta for j in range(len(temp_t))]
                # thêm phần từ 0 vào đầu nhằm mục đích cộng đồn
                p.insert(0, 0)
                p = [p[j] + temp_t[j] for j in range(len(temp_t))]

            flag_direction = -flag_direction
            k += 1
        return p

    # endregion

    # region Gauss II

    def gauss_2_t_coeff(self):
        # lấy chỉ số trung tâm của input x
        middle = int(len(self.x) / 2)
        # khởi tạo 2 biến trái phải nhằm chạy về 2 phía
        left = right = middle
        # biến flag dùng để đỏi hướng
        flag_direction = 1
        # p = y0 + delta(y-1)*t
        p = [delta_y(self.y, middle - 1, middle), self.y[middle]]
        # khởi tạo mảng temp và dùng hoocne nhân
        temp_arr = [0]
        # đánh chỉ số dưới của delta
        delta_index = middle - 1
        # số mũ của delta tương ứng với mẫu là k!
        k = 2
        while (left >= 0) and (right < (len(self.x) - 1)):
            if flag_direction == -1:
                # thay đổi chỉ số dưới của delta khi nhảy sang phải
                delta_index -= 1
                right += 1
                # nhân thêm t - 1, t - 2,... t-n
                temp_arr.append(flag_direction * (delta_index - middle))
                temp_t = hoocne_multiply(temp_arr)
                # tính giá trị hệ số trước t -> nhân vào với mảng hệ só t ở trên
                temp_delta = delta_y(self.y, delta_index, delta_index + k) / factorial(k)
                temp_t = [temp_t[j] * temp_delta for j in range(len(temp_t))]
                # thêm phần từ 0 vào đầu nhằm mục đích cộng đồn
                p.insert(0, 0)
                p = [p[j] + temp_t[j] for j in range(len(temp_t))]
            else:
                left -= 1
                # nhân thêm t + 1, t + 2,...
                temp_arr.append(flag_direction * (delta_index - middle))
                temp_t = hoocne_multiply(temp_arr)
                # tính giá trị hệ số trước t -> nhân vào với mảng hệ só t ở trên
                temp_delta = delta_y(self.y, delta_index, delta_index + k) / factorial(k)
                temp_t = [temp_t[j] * temp_delta for j in range(len(temp_t))]
                # thêm phần từ 0 vào đầu nhằm mục đích cộng đồn
                p.insert(0, 0)
                p = [p[j] + temp_t[j] for j in range(len(temp_t))]

            flag_direction = -flag_direction
            k += 1
        return p

    # endregion

    # region Run

    def run(self):
        self.x, self.y = read_file("../input.txt")
        self.h = self.x[1] - self.x[0]
        self.x0 = self.x[int(len(self.x) / 2)]
        print(f_x(self.gauss_1_t_coeff(), t(2.5, self.x0, self.h)))
        # print(self.bt(1, 0.2, 100, 11.75))
        # print(self.newtoncachdeu_x_solve(2.5))
        print(self.gauss_2_t_coeff())
        # print(self.delta_y(1, 3))
        # print(self.newtonbatky())
        # print(self.hoocne_divive(self.newtonbatky(), 13.5).pop())

    # endregion


if __name__ == '__main__':
    bt = Gauss()
    bt.run()
