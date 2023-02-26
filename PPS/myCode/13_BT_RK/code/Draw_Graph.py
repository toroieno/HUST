from Runghe_Kutta_x import *
from Runghe_Kutta_y import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = RungheKutta_x()
    y = RungheKutta_y()
    print(x.run())
    print(y.run())
    plt.plot(x.run(), y.run())
    plt.show()
