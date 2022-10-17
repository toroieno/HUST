class BT:
  def ReadFile(self):
    f = open('input2.txt', 'r')
    try:
      self.arrHeSoGoc = f.readline().strip().split(' ')
    except:
      print('read file error!')
    finally:
      f.close()
  
  #hien thi ham so
  def PrintF(self, heso):
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
  def HoocnerNguoc(self):
    newArr = [int(num) for num in self.arrHeSoGoc]

    print('    c    |      w_(n+1)(x)      |   he so   \n')
    c = newArr.pop(0)
    arrB = [1, -c]
    print('{:8} | {:20} | {:8}'.format(c, self.PrintF(arrB), str(arrB)))
    arrB.append(0)
    while newArr:
      c = newArr.pop()
      arrA = []
      arrA.append(arrB[0]) #an = bn
      for i in range(1, len(arrB)):
        a_k = arrB[i] - arrB[i-1] * c #a_k = b_k - b_(k+1) * c
        arrA.append(a_k)
      
      print('{:8} | {:20} | {:8}'.format(c, self.PrintF(arrA), str(arrA)))
      arrB = arrA.copy()
      arrB.append(0)

  #main
  def run(self):
    self.ReadFile()
    self.HoocnerNguoc()

#---------------main-----------------
bt = BT()
bt.run()
