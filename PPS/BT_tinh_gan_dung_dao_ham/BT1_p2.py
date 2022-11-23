import numpy as np

class ApproximateDerivative:
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

  def Deg2(self):
    i = len(self.x) - 2
    k = 1
    h = self.x[1] - self.x[0]
    f = np.zeros(len(self.x))
    while i > 0:
      f[k] = (self.y[k+1] - self.y[k-1]) / (2*h)
      print(f[k])
      k += 1
      i -= 1

    # return f[k]

  def Deg3(self):
    pass



  def run(self):
    self.read_file()
    self.Deg2()

#-------------main------------
if __name__ == '__main__':
  bt = ApproximateDerivative()
  bt.run()