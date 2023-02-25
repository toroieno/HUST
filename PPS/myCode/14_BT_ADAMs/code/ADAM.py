from myCode.CasualFunction import *


class Adam:

    # region Initial Variable
    def __init__(self):
        self.x_end = None
        self.h = None
        self.x0 = None
        self.y0 = None
        self.f = None

    # endregion

    # region Input
    def input(self):
        # cho khoảng để tính - input x0 < x < x_end
        self.f = lambda x, y: x * y / 2
        self.y0 = 1
        self.x0 = 0
        self.h = 0.1
        self.x_end = 1

    # endregion

    # region ABs
    def AB(self, order):
        x = np.arange(self.x0, self.x_end + self.h, self.h)
        y = np.zeros(len(x))
        y[0] = self.y0
        if order == 2:
            y[1] = y[0] + self.h / 2 * (3 * self.f(x[0], y[0]) - self.f(x[0] - self.h, self.y0))
            for i in range(2, len(x)):
                y[i] = y[i - 1] + self.h / 2 * (3 * self.f(x[i - 1], y[i - 1]) - self.f(x[i - 2], y[i - 2]))
        elif order == 3:
            y[1] = y[0] + self.h / 12 * (
                        23 * self.f(x[0], y[0]) - 16 * self.f(x[0] - self.h, self.y0) + 5 * self.f(x[0] - 2 * self.h,
                                                                                                   self.y0))
            y[2] = y[1] + self.h / 12 * (
                        23 * self.f(x[1], y[1]) - 16 * self.f(x[0], y[0]) + 5 * self.f(x[0] - self.h, y[0]))
            for i in range(3, len(x)):
                y[i] = y[i - 1] + self.h / 12 * (
                        23 * self.f(x[i - 1], y[i - 1]) - 16 * self.f(x[i - 2], y[i - 2]) + 5 * self.f(x[i - 3],
                                                                                                       y[i - 3]))
        elif order == 4:
            y[1] = y[0] + self.h / 24 * (
                    55 * self.f(x[0], y[0]) - 59 * self.f(x[0] - self.h, self.y0) + 37 * self.f(x[0] - 2 * self.h,
                                                                                                self.y0) - 9 * self.f(
                x[0] - 3 * self.h, self.y0))
            y[2] = y[1] + self.h / 24 * (
                    55 * self.f(x[1], y[1]) - 59 * self.f(x[0], y[0]) + 37 * self.f(x[0] - self.h, y[0]) - 9 * self.f(
                x[0] - 2 * self.h, y[1]))
            y[3] = y[2] + self.h / 24 * (
                    55 * self.f(x[2], y[2]) - 59 * self.f(x[1], y[1]) + 37 * self.f(x[0], y[0]) - 9 * self.f(
                x[0] - self.h, y[0]))
            for i in range(4, len(x)):
                y[i] = y[i - 1] + self.h / 24 * (
                            55 * self.f(x[i - 1], y[i - 1]) - 59 * self.f(x[i - 2], y[i - 2]) + 37 * self.f(x[i - 3], y[
                        i - 3]) - 9 * self.f(x[i - 4], y[i - 4]))
        else:
            raise ValueError("Invalid order")
        return x, y

    # endregion

    # region AMs
    def AM(self, order):
        x = np.arange(self.x0, self.x_end + self.h, self.h)
        y = np.zeros(len(x))
        y[0] = self.y0
        if order == 2:
            for i in range(1, len(x)):
                y_pred = y[i - 1] + self.h / 2 * (self.f(x[i - 1], y[i - 1]) + self.f(x[i], y[i]))
                y[i] = y[i - 1] + self.h / 2 * (self.f(x[i - 1], y[i - 1]) + self.f(x[i], y_pred))
        elif order == 3:
            y[1] = y[0] + self.h / 12 * (5 * self.f(x[0], y[0]) + 8 * self.f(x[1], y[1]) - self.f(x[2], y[2]))
            for i in range(2, len(x)):
                y_pred = y[i - 1] + self.h / 12 * (
                        23 * self.f(x[i - 1], y[i - 1]) - 16 * self.f(x[i - 2], y[i - 2]) + 5 * self.f(x[i - 3],
                                                                                                       y[i - 3]))
                y[i] = y[i - 1] + self.h / 12 * (
                            5 * self.f(x[i], y_pred) + 8 * self.f(x[i - 1], y[i - 1]) - self.f(x[i - 2], y[i - 2]))
        elif order == 4:
            y[1] = y[0] + self.h / 24 * (
                        9 * self.f(x[0], y[0]) + 19 * self.f(x[1], y[1]) - 5 * self.f(x[2], y[2]) + self.f(x[3], y[3]))
            y[2] = y[1] + self.h / 24 * (
                        self.f(x[0], y[0]) - 5 * self.f(x[1], y[1]) + 19 * self.f(x[2], y[2]) + 9 * self.f(x[3], y[3]))
            for i in range(3, len(x)):
                y_pred = y[i - 1] + self.h / 24 * (
                            55 * self.f(x[i - 1], y[i - 1]) - 59 * self.f(x[i - 2], y[i - 2]) + 37 * self.f(x[i - 3], y[
                        i - 3]) - 9 * self.f(x[i - 4], y[i - 4]))
                y[i] = y[i - 1] + self.h / 24 * (
                            9 * self.f(x[i], y_pred) + 19 * self.f(x[i - 1], y[i - 1]) - 5 * self.f(x[i - 2],
                                                                                                    y[i - 2]) + self.f(
                        x[i - 3], y[i - 3]))
        else:
            raise ValueError("Invalid order")
        return x, y

    # endregion

    # region AB-AMs
    def AB_AM(self, order):
        x = np.arange(self.x0, self.x_end + self.h, self.h)
        y = np.zeros(len(x))
        y[0] = self.y0
        if order == 2:
            y[1] = y[0] + self.h * self.f(x[0], y[0])
            for i in range(2, len(x)):
                y[i] = y[i - 1] + self.h / 2 * (3 * self.f(x[i - 1], y[i - 1]) - self.f(x[i - 2], y[i - 2]))
        elif order == 3:
            y[1] = y[0] + self.h * self.f(x[0], y[0])
            y[2] = y[1] + self.h / 2 * (3 * self.f(x[1], y[1]) - self.f(x[0], y[0]))
            for i in range(3, len(x)):
                y[i] = y[i - 1] + self.h / 12 * (
                            23 * self.f(x[i - 1], y[i - 1]) - 16 * self.f(x[i - 2], y[i - 2]) + 5 * self.f(x[i - 3],
                                                                                                           y[i - 3]))
        elif order == 4:
            y[1] = y[0] + self.h * self.f(x[0], y[0])
            y[2] = y[1] + self.h / 2 * (3 * self.f(x[1], y[1]) - self.f(x[0], y[0]))
            y[3] = y[2] + self.h / 12 * (23 * self.f(x[2], y[2]) - 16 * self.f(x[1], y[1]) + 5 * self.f(x[0], y[0]))
            for i in range(4, len(x)):
                y_pred = y[i - 1] + self.h / 24 * (
                            55 * self.f(x[i - 1], y[i - 1]) - 59 * self.f(x[i - 2], y[i - 2]) + 37 * self.f(x[i - 3], y[
                        i - 3]) - 9 * self.f(x[i - 4], y[i - 4]))
                y[i] = y[i - 1] + self.h / 24 * (
                            9 * self.f(x[i], y_pred) + 19 * self.f(x[i - 1], y[i - 1]) - 5 * self.f(x[i - 2],
                                                                                                    y[i - 2]) + self.f(
                        x[i - 3], y[i - 3]))


        else:
            raise ValueError("Invalid order")
        return x, y

    # endregion

    # region Main
    def run(self):
        self.input()

        x, y = self.AB(2)
        print("AB-2 ", x, y)
        x, y = self.AB(3)
        print("AB-3 ", x, y)
        x, y = self.AB(4)
        print("AB-4 ", x, y)

        x, y = self.AM(2)
        print("AM-2 ", x, y)
        x, y = self.AM(3)
        print("AM-3 ", x, y)
        x, y = self.AM(4)
        print("AM-4 ", x, y)

        x, y = self.AB_AM(2)
        print("AB_AM-2 ", x, y)
        x, y = self.AB_AM(3)
        print("AB_AM-3 ", x, y)
        x, y = self.AB_AM(4)
        print("AB_AM-4 ", x, y)

    # endregion


if __name__ == '__main__':
    bt = Adam()
    bt.run()
