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
    except:
      print('Open file error!')
    finally:
      f.close()

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

#-----------------main--------------
if __name__ == '__main__':
  bt = Newton()
  bt.run()