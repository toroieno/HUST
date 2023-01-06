from CasualFunction import *


class Stirling:

    # region Init
    def __init__(self):
        self.x = []
        self.y = []
        self.x0 = None
        self.h = None

    # endregion

    # region Stirling Even

    # S_(2K)
    def stirling_even(self, middle, k):
        begin = middle - k
        end = begin + 2 * k
        delta = delta_y(self.y, begin, end) / factorial(2 * k)
        temp_t = []
        for i in range(1, k + 1):
            temp_t.append((i - 1) ** 2)
        temp_t = hoocne_multiply(temp_t)
        temp_t = [temp_t[j] * delta for j in range(len(temp_t))]

        t_arr = []
        for i in range(len(temp_t) - 1):
            t_arr.append(temp_t[i])
            t_arr.append(0.0)
        t_arr.append(temp_t[-1])

        return t_arr

    # endregion

    # region Stirling Odd

    # S_(2k+1)
    def stirling_odd(self, middle, k):
        begin = middle - k - 1
        end = begin + (2 * k + 1)
        delta_1 = delta_y(self.y, begin, end)
        delta_2 = delta_y(self.y, begin + 1, end + 1)
        delta = (delta_1 + delta_2) / (factorial(2 * k + 1) * 2)
        temp_t = []
        for i in range(1, k + 1):
            temp_t.append(i ** 2)
        temp_t = hoocne_multiply(temp_t)
        temp_t = [temp_t[j] * delta for j in range(len(temp_t))]

        t_arr = []
        for i in range(len(temp_t)):
            t_arr.append(temp_t[i])
            t_arr.append(0.0)

        return t_arr

    # endregion

    # region Main

    # all
    def stirling(self):
        middle = int(len(self.x) / 2)
        init_value = (delta_y(self.y, middle - 1, middle) + delta_y(self.y, middle, middle + 1)) / 2
        p = np.zeros(len(self.x) - 2).tolist()
        p.append(init_value)
        p.append(self.y[middle])
        count_even = middle + 1
        count_odd = count_even - 1
        for k in range(1, count_odd):
            s_odd = self.stirling_odd(middle, k)
            for i in range(len(s_odd)):
                p[-i - 1] += s_odd[len(s_odd) - i - 1]
        for k in range(1, count_even):
            s_even = self.stirling_even(middle, k)
            for i in range(len(s_even)):
                p[-i - 1] += s_even[len(s_even) - i - 1]

        return p

    def run(self):
        self.x, self.y = read_file("../input.txt")
        self.h = self.x[1] - self.x[0]
        self.x0 = self.x[int(len(self.x) / 2)]
        # print(self.x[middle])
        print('he so: ', self.stirling())
        print(f_x(self.stirling(), t(5.5, self.x0, 1)))

    # endregion


if __name__ == '__main__':
    bt = Stirling()
    bt.run()
