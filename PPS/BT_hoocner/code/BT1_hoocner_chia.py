from CasualFunction import *
class BT:
  def read_file(self):
    f = open('../input1.txt', 'r')
    try:
      self.arr_he_so_goc = f.readline().strip().split(' ')
      self.c = int(f.readline())
    except:
      print('error when read file!')
    finally:
      f.close()
  def factorial(self, x):
    if x == 0:
      return 1
    return self.factorial(x-1) * x
  #Qn(c) - tinh gia tri ham bac n tai c
  def Q(self, coeff, c):
    mu = len(coeff) - 1
    f = 0
    for i in coeff:
      f += i * c**mu
      mu -= 1
    return f
  #bai tap 1: Pn(c), Pn(c)/(x-c), P(k)(c)
  def hoocner_xuoi(self):
    arrA = self.arr_he_so_goc
    lenArr = len(self.arr_he_so_goc)
    k = 1
    print('he so k  |    Pn(c)   |  \t\t   Pn(c)/(x-c)   \t\t   |  P(k)(c)  ')
    print('_'*8+' | '+'_'*10+' | '+'_'*50+' | '+'_'*8)
    while k < lenArr:
      bac = lenArr - k #bac cua phuong trinh hien tai
      arrB = [] 
      arrB.append(int(arrA[0])) #bn = an
      for i in range(1, bac+1):
        b_k = int(arrA[i]) + arrB[i-1] * self.c #b_k = a_k + b_(k+1) * c
        arrB.append(b_k)
      
      P1 = arrB.pop(-1) #Pn(c)
      P2 = self.Q(arrB, self.c)*self.factorial(k) #P(k)(c)

      print('{:8} | {:10} | {:50} | {:8}'.format(k, P1, str(arrB), P2))

      arrA = arrB
      k = k + 1
  
  #main
  def run(self):
    self.read_file()
    self.hoocner_xuoi()

#-------------main-------------
bt = BT()
bt.run()