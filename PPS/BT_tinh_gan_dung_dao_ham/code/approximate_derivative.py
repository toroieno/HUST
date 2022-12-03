import numpy as np

class ApproximateDerivative:
  def read_file(self):
    try:
      f = open("../input.txt", "r")
      self.x = []
      self.y = []
      all_arr = f.read().split("\n")
      while all_arr[-1] == '':
        all_arr.pop()
      for each in all_arr:
        arr = each.split(" ")
        self.x.append(float(arr[0]))
        self.y.append(float(arr[1]))
      self.h = self.x[1] - self.x[0]
    except:
      print('Open file error!')
    finally:
      f.close()

  #dao ham cap 1, n = 2, 3 moc
  def Deg2(self):
    print('Tính đạo hàm với 3 mốc (n = 2): ')
    if (len(self.x) < 3):
      print('cần ít nhất 3 mốc')
      return
    k = 1
    # h = self.x[1] - self.x[0]
    # f = np.zeros(len(self.x))
    while k < len(self.x) - 1:
      f = (self.y[k+1] - self.y[k-1]) / (2*self.h)
      print('mốc [{0}, {1}, {2}]: tinh \n f\'({3})= {4}'.format(self.x[k-1], self.x[k], self.x[k+1], self.x[k], f))
      k += 1

    # return f[k]

  #dao ham cap 1, n = 3, 4 moc
  def Deg3(self):
    print('Tính đạo hàm với 4 mốc (n = 3): ')
    if (len(self.x) < 4):
      print('cần ít nhất 4 mốc')
      return
    k = 1
    # h = self.x[1] - self.x[0]
    # f = np.zeros(len(self.x))
    #moc [x_0, x_1, x_2, x_3]
    while k < len(self.x) - 2:
      f1 = (-2*self.y[k-1] - 3*self.y[k] + 6*self.y[k+1] - self.y[k+2]) / (6*self.h) #trung tam f(x_1)
      f2 = (self.y[k-1] - 6*self.y[k] + 3*self.y[k+1] + 2*self.y[k+2]) / (6*self.h) #trung tam f(x_2)
      print('moc [{0}, {1}, {2}, {3}]: tinh \n f\'({6})= {4} \n f\'({7})= {5}'.format(self.x[k-1], self.x[k], self.x[k+1], self.x[k+2], f1, f2, self.x[k], self.x[k+1]))
      k += 1

  def run(self):
    self.read_file()
    # self.Deg1()
    self.Deg2()
    self.Deg3()

#-------------main------------
if __name__ == '__main__':
  bt = ApproximateDerivative()
  bt.run()