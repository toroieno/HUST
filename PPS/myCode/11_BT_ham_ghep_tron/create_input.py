from math import *

def g(x):
  return 3 * x**3 + 2 * x**2 - 3*x + 3
  # return 2 * x**2 - 3*x + 3
  # return sin(x)
  # return x**2
  # return 2*x+1
  # return 1 / (1 + x**2)
  # return 2 * x
 
def write_file(a, b, kc):
  try:
    f = open('input.txt', 'w')
    k = a
    while k < b:
      y = g(k)
      f.write("{} {}\n".format(k, y))
      k = k + kc
    # for i in range(b, a, -1):
    #   y = g(i)
    #   f.write("{} {}\n".format(i, y))
  except:
    print('read file error!')
  finally:
    f.close()


if __name__ == '__main__':
  write_file(-2, 10, 2)