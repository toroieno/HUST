from CasualFunction import *


class Euler:

    # region Initial Variable
    def __init__(self):
        self.eps = None
        self.xf = None
        self.h = None
        self.x0 = None
        self.y0 = None
        self.f = None
    # endregion

    # region Euler with range
    def euler_forward(self):
        """Implementation of Euler's Forward method for solving ODEs"""
        x = np.arange(self.x0, self.xf + self.h, self.h)
        y = np.zeros_like(x)
        y[0] = self.y0
        for i in range(len(x) - 1):
            y[i + 1] = y[i] + self.h * self.f(x[i], y[i])
        return x, y

    def euler_backward(self):
        """Implementation of Euler's Backward method for solving ODEs"""
        x = np.arange(self.x0, self.xf + self.h, self.h)
        y = np.zeros_like(x)
        y[0] = self.y0
        for i in range(len(x) - 1):
            y[i + 1] = y[i] + self.h * self.f(x[i + 1], y[i + 1])
        return x, y

    def trapezoidal(self):
        """Implementation of the Trapezoidal method for solving ODEs"""
        x = np.arange(self.x0, self.xf + self.h, self.h)
        y = np.zeros_like(x)
        y[0] = self.y0
        for i in range(len(x) - 1):
            y[i + 1] = y[i] + (self.h / 2) * (self.f(x[i], y[i]) + self.f(x[i + 1], y[i] + self.h * self.f(x[i], y[i])))
        return x, y
    # endregion

    # region Euler with eps
    def euler_forward_eps(self):
        """Implementation of Euler's Forward method for solving ODEs"""
        def euler_step(f, x, y, h):
            return y + h * f(x, y)

        x = self.x0
        y = self.y0
        t = [x]
        y_values = [y]

        while x < (1 - self.eps) * self.xf:
            y_next = euler_step(self.f, x, y, self.h)
            y = y_next
            x = x + self.h
            t.append(x)
            y_values.append(y)

        return np.array(t), np.array(y_values)

    def euler_backward_eps(self):
        """Implementation of Euler's Backward method for solving ODEs"""
        def backward_step(f, x, y, h):
            return y + h * f(x + h, y + h * f(x, y))

        x = self.x0
        y = self.y0
        t = [x]
        y_values = [y]

        while x < (1 - self.eps) * self.xf:
            y_next = backward_step(self.f, x, y, self.h)
            y = y_next
            x = x + self.h
            t.append(x)
            y_values.append(y)

        return np.array(t), np.array(y_values)

    def trapezoidal_eps(self):
        """Implementation of the Trapezoidal method for solving ODEs"""
        def trapezoidal_step(f, x, y, h):
            return y + (h / 2) * (f(x, y) + f(x + h, y + h * f(x, y)))

        x = self.x0
        y = self.y0
        t = [x]
        y_values = [y]

        while x < (1 - self.eps) * self.xf:
            y_next = trapezoidal_step(self.f, x, y, self.h)
            y = y_next
            x = x + self.h
            t.append(x)
            y_values.append(y)

        return np.array(t), np.array(y_values)

    # endregion

    # region Input
    def input(self, option):
        # cho khoảng để tính - input x0 < x < xf
        if option == 1:
            self.f = lambda x, y: x + y
            self.y0 = 1
            self.x0 = 0
            self.h = 1 / 20
            self.xf = 0.5

        # cho sai số eps, tính tại y(xf)
        elif option == 2:
            self.f = lambda x, y: x + y
            self.y0 = 1
            self.x0 = 0
            self.h = 1 / 20
            self.eps = 10e-4  # sai số cho phép
            self.xf = 0.1  # giá trị cần tính

    # endregion

    # region Main
    def run(self):
        option = 2  # chọn 1 hoặc 2
        self.input(option)

        if option == 1:
            x, y = self.euler_forward()
            print('Euler hiện: \n x = {0} \n y = {1}'.format(x, y))
            x, y = self.euler_backward()
            print('Euler ẩn: \n x = {0} \n y = {1}'.format(x, y))
            x, y = self.trapezoidal()
            print('Công thức hình thang: \n x = {0} \n y = {1}'.format(x, y))
        elif option == 2:
            # Solve the ODE using Euler's Forward method
            t_euler_forward, y_euler_forward = self.euler_forward_eps()

            # Solve the ODE using Euler's Backward method
            t_euler_backward, y_euler_backward = self.euler_backward_eps()

            # Solve the ODE using the Trapezoidal method
            t_trapezoidal, y_trapezoidal = self.trapezoidal_eps()

            # Print the solutions at the final time step
            print("Euler hiện: y({:.1f}) = {:.4f}".format(t_euler_forward[-1], y_euler_forward[-1]))
            print("Euler ẩn: y({:.1f}) = {:.4f}".format(t_euler_backward[-1], y_euler_backward[-1]))
            print("Công thức hình thang: y({:.1f}) = {:.4f}".format(t_trapezoidal[-1], y_trapezoidal[-1]))

    # endregion


if __name__ == '__main__':
    bt = Euler()
    bt.run()
