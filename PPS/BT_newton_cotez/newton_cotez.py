from CasualFunction import *


class NC:
    def __init__(self):
        self.x = []
        self.y = []
        self.a = None
        self.b = None

    def H_i(self, i):
        pass

    def main(self, n):
        result = 0
        if n == 1:
            result = (self.b - self.a) / 2 * (self.y[0] + self.y[1])

        return result

    def run(self):
        self.x, self.y = read_file('input.txt')
        self.a = self.x[0]
        self.b = self.x[-1]
        print(self.a, self.b)
        print(self.main(1))


if __name__ == "__main__":
    bt = NC()
    bt.run()
