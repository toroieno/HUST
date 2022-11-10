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

  #ti sai phan - de quy
  def ty_sai_phan(self, a, b):
    if b - a == 1:
      return (self.y[b] - self.y[a]) / (self.x[b] - self.x[a])
    return (self.ty_sai_phan(a+1,b) - self.ty_sai_phan(a,b-1)) / (self.x[b] - self.x[a])

  # bang ty hieu
  def bang_ty_hieu(self):
    l = len(self.x)
    # BTH = np.zeros([l, l]).tolist()
    BTH = np.zeros([l, l])
    #khoi tao ty sai phan
    for i in range(l):
      BTH[i, 0] = self.y[i]
    #tao ty sai phan cac cap - row
    for col in range(1, l):
      for row in range(col, l):
        BTH[row, col] = (BTH[row, col - 1] - BTH[row - 1, col - 1]) / (self.x[row] - self.x[row - col])

    return BTH

  #them moc moi
  def add_new_point(self, x, y, BTH):
    # BTH = BTH.astype(object)
    BTH[0].append(0)
    print(BTH[0])
    # bth = np.append(BTH[0], 0)
    # BTH[0] = bth
    # print(BTH[0])
    # BTH[0].append(0)
    # BTH = [bth.append(0) for bth in BTH]
    # len_bth = len(BTH)
    # new_row = np.zeros(len(BTH[0]))
    # new_row[0] = x
    # new_row[1] = y
    # for i in range(2, len(new_row)):
    #   new_row[i] = (y - BTH[-1][0]) / (x - self.x[len_bth + 1 - i])

    # BTH.append(new_row)

  def newton_moc_bat_ky(self, x0):
    x = Symbol('x')
    p = self.y[0]
    w = 1
    length = len(self.x)
    for i in range(1, length):
      w = w * (x - self.x[i-1])
      p_i = self.ty_sai_phan(0,i)*w
      p = p + p_i
    value = p.subs(Symbol('x'), x0)
    return p, value

  def newton_tien(self):
    pass
  def newton_lui(self):
    pass
  # def newton_tien_lui(self, x0):
  #   tien = abs(self.x[0] - x0)
  #   lui = abs(self.x[-1] - x0)
  #   if tien > lui:
  #     self.newton_lui()
  #   else:
  #     self.newton_tien()

  def draw_graph(self, f):
    x = np.array(self.x)
    y = np.array(self.y)

    plt.scatter(x, y)
    xpoints = np.linspace(min(self.x) - .5, max(self.x) + .5, 1000)
    ypoints = [f.subs(Symbol('x'), xt) for xt in xpoints]
    plt.plot(xpoints, ypoints)
    plt.savefig('graph.png')
    # plt.show()
  #main
  def run(self):
    self.read_file()
    # f, value = self.newton_moc_bat_ky(4)
    # print(simplify(f))
    # # print('{:.2f}'.format(value))
    # self.draw_graph(f)
    # print(self.bang_ty_hieu())
    BTH = self.bang_ty_hieu()
    print(BTH)
    print(self.ty_sai_phan(0, 2))
    # self.add_new_point(7, 10 , BTH)
    # print(BTH)


#-----------------main--------------
if __name__ == '__main__':
  bt = Newton()
  bt.run()