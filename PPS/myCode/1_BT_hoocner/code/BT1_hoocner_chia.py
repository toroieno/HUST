import sys 
sys.path.insert(1, '../../../')
from myCode.CasualFunction import *

class BT:
  # region variables
  def __init__(self):
    self.arr_coeffs = []
    self.c = None
  # endregion

  # region read file
  def read_file(self):
    f = open('../input1.txt', 'r')
    self.arr_coeffs = f.readline().strip().split(' ')
    self.arr_coeffs = [float(self.arr_coeffs[i]) for i in range(len(self.arr_coeffs))]  # change string to float number
    self.c = float(f.readline())

    f.close()
  # endregion

  # region main algorithm
  def hoocner_divide(self):
    b = [self.arr_coeffs[0]] # bn = an
    for i in range(1, len(self.arr_coeffs)):
        b_k = self.arr_coeffs[i] + b[i - 1] * self.c  # b_k = a_k + b_k-1 * c
        b.append(float(b_k))

    return b
  # endregion
  
  # region bai tap 1: Pn(c), Pn(c)/(x-c), P(k)(c)
  def other_func(self):
    while True:
      print('='*50)
      print('1. tính giá trị hàm P(x0)')
      print('2. tính đạo hàm bậc k của P(x) tại x0')
      option = int(input('options: '))
      match option:
        case 1:
          self.p_x()
        case 2:
          self.p_k()
        case _:
          break
    print('end')
  
  # tính giá trị hàm số
  def p_x(self):
    x0 = float(input('x0 = '))
    p = self.hoocner_divide()
    p.pop()
    f = f_x(p, x0)
    print('f(x0) = f({:1}) = {:2}'.format(x0, f))

  # tính đạo hàm bậc k
  def p_k(self):
    k = int(input('k = '))
    x0 = float(input('x0 = '))
    p = self.hoocner_divide()
    p.pop()
    f = Degf_k(p, k, x0)
    print('f(k)(x0) = f({:1})({:2}) = {:3}'.format(k, x0, f))

  # endregion
  
  # region main
  def run(self):
    self.read_file()
    p = self.hoocner_divide()
    p.pop()
    print('P(x) = ', p)
    self.other_func()

  # endregion

#-------------main-------------
if __name__ == "__main__":
  bt = BT()
  bt.run()