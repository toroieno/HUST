class BT:
  
  # region variables
  def __init__(self):
    self.arr_coeffs = []

  # endregion
  
  # region input
  def read_file(self):
    f = open('../input2.txt', 'r')
    self.arr_coeffs = f.readline().strip().split(' ')

    f.close()
  # endregion

  # region hien thi ham so
  def print_f(self, coeff):
    f = ''
    mu = len(coeff) - 1
    for each in coeff:
      if mu > 1:
        f += str(each) + 'x^' + str(mu) + ' + '
      elif mu == 1:
        f += str(each) + 'x' + ' + '
      else:
        f += str(each)
      mu -= 1
    return f
    
  # endregion 

  #bai tap 2: tinh w_(n+1)(x)
  def hoocner_multi(self):
    newArr = [int(num) for num in self.arr_coeffs]

    print('    c   |   \t\t  w_(n+1)(x)\t\t\t   |  he so   ')
    print('-'*8+'|'+'-'*50+'|'+'-'*8)
    c = newArr.pop(0)
    arrB = [1, -c]
    print('{:8}|{:50}|{:16}'.format(c, self.print_f(arrB), str(arrB)))
    
    arrB.append(0)
    while newArr:
      c = newArr.pop(0)
      arrA = []
      arrA.append(arrB[0]) #an = bn
      for i in range(1, len(arrB)):
        a_k = arrB[i] - arrB[i-1] * c #a_k = b_k - b_(k+1) * c
        arrA.append(a_k)
      
      print('{:8}|{:50}|{:16}'.format(c, self.print_f(arrA), str(arrA)))
      arrB = arrA.copy()
      arrB.append(0)

  # region main
  def run(self):
    self.read_file()
    self.hoocner_multi()

  # endregion

#---------------main-----------------
if __name__ == '__main__':
  bt = BT()
  bt.run()
