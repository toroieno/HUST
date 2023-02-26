from myCode.CasualFunction import *


class RungheKutta:

    # region Initial Variable
    def __init__(self):
        self.x_end = None
        self.h = None
        self.x0 = None
        self.y0 = None
        self.f = None

    # endregion

    # region R-K 2
    def rk2(self):
        """
        Solve the ODE y' = f(x, y) using RK2 method.

        Parameters:
            f: function of two variables, the derivative function f(x, y)
            x0: initial x value
            y0: initial y value
            x_end: end x value
            h: step size

        Returns:
            X: array of x values
            Y: array of corresponding y values
        """
        X = [self.x0]
        Y = [self.y0]
        while X[-1] < self.x_end:
            x = X[-1]
            y = Y[-1]
            k1 = self.h * self.f(x, y)
            k2 = self.h * self.f(x + self.h, y + k1)
            Y.append(y + 0.5 * (k1 + k2))
            X.append(x + self.h)

        return np.array(X), np.array(Y)

    # endregion

    # region R-K 3
    def rk3(self):
        """
        Solve the ODE y' = f(x, y) using RK3 method.

        Parameters:
            f: function of two variables, the derivative function f(x, y)
            x0: initial x value
            y0: initial y value
            x_end: end x value
            h: step size

        Returns:
            X: array of x values
            Y: array of corresponding y values
        """
        X = [self.x0]
        Y = [self.y0]
        while X[-1] < self.x_end:
            x = X[-1]
            y = Y[-1]
            k1 = self.h * self.f(x, y)
            k2 = self.h * self.f(x + 0.5 * self.h, y + 0.5 * k1)
            k3 = self.h * self.f(x + self.h, y - k1 + 2 * k2)
            Y.append(y + (1 / 6) * (k1 + 4 * k2 + k3))
            X.append(x + self.h)

        return np.array(X), np.array(Y)

    # endregion

    # region R-K 4
    def rk4(self):
        """
        Solve the ODE y' = f(x, y) using RK4 method.

        Parameters:
            f: function of two variables, the derivative function f(x, y)
            x0: initial x value
            y0: initial y value
            x_end: end x value
            h: step size

        Returns:
            X: array of x values
            Y: array of corresponding y values
        """
        X = [self.x0]
        Y = [self.y0]
        while X[-1] < self.x_end:
            x = X[-1]
            y = Y[-1]
            k1 = self.h * self.f(x, y)
            k2 = self.h * self.f(x + 0.5 * self.h, y + 0.5 * k1)
            k3 = self.h * self.f(x + 0.5 * self.h, y + 0.5 * k2)
            k4 = self.h * self.f(x + self.h, y + k3)
            Y.append(y + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4))
            X.append(x + self.h)

        return np.array(X), np.array(Y)

    # endregion

    # region Input
    def input(self):
        # cho khoảng để tính - input x0 < x < x_end
        # self.f = lambda x, y: -0.35*y + (0.35*x*x*y) / (1+15*x*x)
        self.f = lambda x, y: 1.5*(1-x/25)*x-(0.5*x*x*y)/(1+15*x*x)
        self.y0 = 6
        self.x0 = 0
        self.h = 0.1
        self.x_end = 10

    # endregion

    # region Draw Graph
    def draw_graph(self):
        # Solve the differential equation using RK2, RK3, and RK4 methods
        x_rk2, y_rk2 = self.rk2()
        x_rk3, y_rk3 = self.rk3()
        x_rk4, y_rk4 = self.rk4()

        # Plot the results
        plt.plot(x_rk2, y_rk2, label='RK2', color="red")
        plt.plot(x_rk3, y_rk3, label='RK3', color="blue")
        plt.plot(x_rk4, y_rk4, label='RK4', color="green")
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
    # endregion
    # region Main
    def run(self):
        self.input()
        x_rk2, y_rk2 = self.rk2()
        print('rk2: \n x = {0} \n y =  {1}'.format(x_rk2, y_rk2))
        x_rk3, y_rk3 = self.rk3()
        print('rk3: \n x = {0} \n y =  {1}'.format(x_rk3, y_rk3))
        x_rk4, y_rk4 = self.rk4()
        print('rk4: \n x = {0} \n y =  {1}'.format(x_rk4, y_rk4))
        self.draw_graph()

    # endregion


if __name__ == '__main__':
    bt = RungheKutta()
    bt.run()
