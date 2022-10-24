import matplotlib.pyplot as plt
import numpy as np

class Lagrange:
  def read_file(self):
    try:
      f = open("input.txt", "r")
      self.x = []
      self.y = []
      all_arr = f.read().split("\n")
      for each in all_arr:
        arr = each.split(" ")
        self.x.append(float(arr[0]))
        self.y.append(float(arr[1]))
    except:
      print('Open file error!')
    finally:
      f.close()
  #tinh ham f(x) bac n
  def f(self, x, coeff):
    y = 0
    leng = len(coeff)
    for i in range(leng):
      y += coeff[i] * x ** (leng - i - 1)

    return y

  def D_i(self, index):
    x_i = self.x[index]
    d_i = 1
    for i in range(0, len(self.x)):
      if i != index:
        d_i *= (x_i - self.x[i])
    return d_i

  #tinh w_(n+1)(x)
  def hoocner_nhan(self):
    newArr = [i for i in self.x]

    c = newArr.pop(0)
    arrB = [1, -c]   
    arrB.append(0)
    while newArr:
      c = newArr.pop()
      arrA = []
      arrA.append(arrB[0]) #an = bn
      for i in range(1, len(arrB)):
        a_k = arrB[i] - arrB[i-1] * c #a_k = b_k - b_(k+1) * c
        arrA.append(a_k)
      arrB = arrA.copy()
      arrB.append(0)
    
    arrB.pop(-1)
    return arrB

  #tinh w_(n+1)(x)/(x-x_i)
  def hoocner_chia(self, arr, index):
    arrA = [i for i in arr]
    c = self.x[index]

    arrB = []
    arrB.append(arrA[0]) #bn = an
    for i in range(1, len(arrA)):
      b_k = arrA[i] + arrB[i-1] * c #b_k = a_k + b_(k+1) * c
      arrB.append(b_k)

    arrB.pop(-1)
    print(arrB)
    return arrB

  #tinh P_n(x)
  def lagrange(self):
    self.w_n = np.zeros(len(self.x))

    loop = len(self.x)
    for i in range(0, loop):
      w = [(w_i * self.y[i] / self.D_i(i)) for w_i in self.hoocner_chia(self.hoocner_nhan(), i)] #ct2 lagrange
      # print(w)
      for j in range(0, loop):
        self.w_n[j] += w[j]

    print(self.w_n)
  
  def draw_graph(self):
    x = np.array(self.x)
    y = np.array(self.y)

    plt.scatter(x, y)
    xpoints = np.linspace(self.x[0]-0.5, self.x[len(self.w_n) - 1] + 0.5, 1000)
    plt.plot(xpoints, self.f(xpoints, self.w_n))
    # plt.savefig("mygraph.png")
    plt.show()
    
  #main
  def run(self):
    self.read_file()
    self.lagrange()
    self.draw_graph()

#--------------------main--------------------
if __name__ == '__main__':
  bt = Lagrange()
  bt.run()