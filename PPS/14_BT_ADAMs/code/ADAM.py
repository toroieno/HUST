from CasualFunction import *


class Adam:

    # region Initial Variable
    def __init__(self):
        self.x_end = None
        self.h = None
        self.x0 = None
        self.y0 = None
        self.f = None

    # endregion

    #region AB
    def ab2(f, x0, y0, x_end, h):
        # Initialize time array and solution array
        t = np.arange(x0, x_end + h, h)
        y = np.zeros_like(t)
        y[0] = y0

        # Solve for the first two points using Runge-Kutta method
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h, y0 + k1)
        y[1] = y[0] + 0.5 * (k1 + k2)

        # Solve for subsequent points using AB2
        for i in range(1, len(t) - 1):
            y[i + 1] = y[i] + h * (1.5 * f(t[i], y[i]) - 0.5 * f(t[i - 1], y[i - 1]))

        return t, y

    def ab3(f, x0, y0, x_end, h):
        # Initialize time array and solution array
        t = np.arange(x0, x_end + h, h)
        y = np.zeros_like(t)
        y[0] = y0

        # Solve for the first three points using Runge-Kutta method
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h, y0 + k1)
        k3 = h * f(x0 + 2 * h, y0 + 2 * k2 - k1)
        y[1] = y[0] + 0.5 * (k1 + k2)
        y[2] = y[1] + (h / 12) * (23 * k3 - 16 * k2 + 5 * k1)

        # Solve for subsequent points using AB3
        for i in range(2, len(t) - 1):
            y[i + 1] = y[i] + (h / 12) * (23 * f(t[i], y[i]) - 16 * f(t[i - 1], y[i - 1]) + 5 * f(t[i - 2], y[i - 2]))

        return t, y

    def ab4(f, x0, y0, x_end, h):
        # Initialize time array and solution array
        t = np.arange(x0, x_end + h, h)
        y = np.zeros_like(t)
        y[0] = y0

        # Solve for the first four points using Runge-Kutta method
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h, y0 + k1)
        k3 = h * f(x0 + 2 * h, y0 + 2 * k2 - k1)
        k4 = h * f(x0 + 3 * h, y0 + 3 * k3 - 3 * k2 + k1)
        y[1] = y[0] + (h / 24) * (55 * k1 - 59 * k2 + 37 * k3 - 9 * k4)
        y[2] = y[1] + (h / 24) * (9 * f(x0 + 2 * h, y[1]) + 19 * k1 - 5 * k2 + k3)
        y[3] = y[2] + (h / 24) * (55 * f(x0 + 2 * h, y[1]) - 59 * f(x0 + h, y0 + k1) + 37 * k2 - 9 * k3)

        # Solve for subsequent points using AB4
        for i in range(3, len(t) - 1):
            y[i + 1] = y[i] + (h / 24) * (
                        55 * f(t[i], y[i]) - 59 * f(t[i - 1], y[i - 1]) + 37 * f(t[i - 2], y[i - 2]) - 9 * f(t[i - 3],
                                                                                                             y[i - 3]))

        return t, y
    #endregion

    #region AM


    #endregion

    # region AB_AM
    def abam2(self):
        # Initialize time array and solution array
        t = np.arange(self.x0, self.x_end + self.h, self.h)
        y = np.zeros_like(t)
        y[0] = self.y0

        # Solve for the second point using AB2
        y[1] = y[0] + self.h * self.f(self.x0, self.y0)

        # Solve for subsequent points using AM2
        for i in range(1, len(t) - 1):
            y_pred = y[i] + self.h * (1.5 * self.f(t[i], y[i]) - 0.5 * self.f(t[i - 1], y[i - 1]))
            y[i + 1] = y[i] + self.h * (0.5 * self.f(t[i + 1], y_pred) + 0.5 * self.f(t[i], y[i]))

        return t, y

    def abam3(self):
        # Initialize time array and solution array
        t = np.arange(self.x0, self.x_end + self.h, self.h)
        y = np.zeros_like(t)
        y[0] = self.y0

        # Solve for the first two points using AB2
        y[1] = y[0] + self.h * self.f(self.x0, self.y0)
        y[2] = y[1] + self.h * self.f(t[1], y[1])

        # Solve for subsequent points using AM3
        for i in range(2, len(t) - 1):
            y_pred = y[i] + self.h * (23 / 12 * self.f(t[i], y[i]) - 4 / 3 * self.f(t[i - 1], y[i - 1]) + 5 / 12 * self.f(t[i - 2], y[i - 2]))
            y[i + 1] = y[i] + self.h * (5 / 12 * self.f(t[i + 1], y_pred) + 2 / 3 * self.f(t[i], y[i]) - 1 / 12 * self.f(t[i - 1], y[i - 1]))

        return t, y

    def abam4(self):
        # Initialize time array and solution array
        t = np.arange(self.x0, self.x_end + self.h, self.h)
        y = np.zeros_like(t)
        y[0] = self.y0

        # Solve for the first four points using AB4
        y[1] = y[0] + self.h * self.f(self.x0, self.y0)
        y[2] = y[1] + self.h * self.f(t[1], y[1])
        y[3] = y[2] + self.h * self.f(t[2], y[2])
        y[4] = y[3] + self.h * self.f(t[3], y[3])

        # Solve for subsequent points using AM4
        for i in range(4, len(t) - 1):
            y_pred = y[i] + self.h * (55 / 24 * self.f(t[i], y[i]) - 59 / 24 * self.f(t[i - 1], y[i - 1]) + 37 / 24 * self.f(t[i - 2], y[
                i - 2]) - 9 / 24 * self.f(t[i - 3], y[i - 3]))
            y[i + 1] = y[i] + self.h * (9 / 24 * self.f(t[i + 1], y_pred) + 19 / 24 * self.f(t[i], y[i]) - 5 / 24 * self.f(t[i - 1], y[
                i - 1]) + 1 / 24 * self.f(t[i - 2], y[i - 2]))

        return t, y

    # endregion

    # region Input
    def input(self):
        # cho khoảng để tính - input x0 < x < x_end
        self.f = lambda x, y: x + y
        self.y0 = 1
        self.x0 = 0
        self.h = 0.1
        self.x_end = 0.5

    # endregion

    # region Main
    def run(self):
        self.input()
        t, y = self.abam2()
        print('abam 2: x = {0}, y = {1}'.format(t, y))
        t, y = self.abam3()
        print('abam 3: x = {0}, y = {1}'.format(t, y))
        t, y = self.abam4()
        print('abam 4: x = {0}, y = {1}'.format(t, y))

    # endregion


if __name__ == '__main__':
    bt = Adam()
    bt.run()
