class BT:
  def read_file(self):
    f = open('input2.txt', 'r')
    try:
      self.arr_he_so_goc = f.readline().strip().split(' ')
    except:
      print('read file error!')
    finally:
      f.close()
  
  #hien thi ham so
  def print_f(self, heso):
    f = ''
    mu = len(heso) - 1
    for each in heso:
      if mu > 1:
        f += str(each) + 'x^' + str(mu) + ' + '
      elif mu == 1:
        f += str(each) + 'x' + ' + '
      else:
        f += str(each)
      mu -= 1
    return f
  #bai tap 2: tinh w_(n+1)(x)
  def hoocner_nguoc(self):
    newArr = [int(num) for num in self.arr_he_so_goc]

    print('    c    |    \t\t  w_(n+1)(x)  \t\t    |   he so   \n')
    c = newArr.pop(0)
    arrB = [1, -c]
    print('{:8} | {:40} | {:8}'.format(c, self.print_f(arrB), str(arrB)))
    arrB.append(0)
    while newArr:
      c = newArr.pop()
      arrA = []
      arrA.append(arrB[0]) #an = bn
      for i in range(1, len(arrB)):
        a_k = arrB[i] - arrB[i-1] * c #a_k = b_k - b_(k+1) * c
        arrA.append(a_k)
      
      print('{:8} | {:40} | {:8}'.format(c, self.print_f(arrA), str(arrA)))
      arrB = arrA.copy()
      arrB.append(0)

  #main
  def run(self):
    self.read_file()
    self.hoocner_nguoc()

#---------------main-----------------
bt = BT()
bt.run()
