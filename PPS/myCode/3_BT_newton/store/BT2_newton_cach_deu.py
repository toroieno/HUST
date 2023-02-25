import matplotlib.pyplot as plt
import numpy as np
from sympy import *

class Newton:
  def read_file(self):
    try:
      f = open("input.txt", "r")
      self.x = []
      self.y = []
      all_arr = f.read().split("\n")
      while all_arr[-1] == '':
        all_arr.pop()
      for each in all_arr:
        arr = each.split(" ")
        self.x.append(float(arr[0]))
        self.y.append(float(arr[1]))
      #khoang cach deu cac moc
      self.h = self.x[1] - self.x[0]
    except:
      print('Open file error!')
    finally:
      f.close()

  #tinh giai thua
  def factorial(self, n):
    if n == 0:
      return 1
    return n * self.factorial(n-1)

  def delta(self, k, hat):
    if hat == 1:
      return self.y[k+1] - self.y[k]
    return self.delta(k+1, hat-1) - self.delta(k, hat-1)

  #tinh ty sai phan y[x_i,x_j]
  def ty_sai_phan(self, begin, end):
    hat = end - begin + 1
    return self.delta(begin, hat-1) / (self.factorial(hat-1) * pow(self.h, hat))

  def newton_cach_deu(self):
    pass
  
  def draw_graph(self, f):
    x = np.array(self.x)
    y = np.array(self.y)

    plt.scatter(x, y)
    xpoints = np.linspace(min(self.x) - .5, max(self.x) + .5, 1000)
    ypoints = [f.subs(Symbol('x'), xt) for xt in xpoints]
    plt.plot(xpoints, ypoints)
    # plt.savefig('graph.png')
    plt.show()
  #main
  def run(self):
    self.read_file()
    print(self.ty_sai_phan(0, 2))
    print('fac:', self.factorial(5))

#-----------------main--------------
if __name__ == '__main__':
  bt = Newton()
  bt.run()