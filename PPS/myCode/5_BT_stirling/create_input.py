from math import *

def g(x):
  # return 2 * x**2 - 3*x + 3
  # return sin(x)
  return float(x**2)
 
def write_file(a, b, kc):
  try:
    f = open('input.txt', 'w')
    k = a
    while k < b:
      y = g(k)
      f.write("{} {}\n".format(k, y))
      k = k + kc
    # for i in range(a, b):
    #   y = g(i)
    #   f.write("{} {}\n".format(i, y))
  except:
    print('read file error!')
  finally:
    f.close()


if __name__ == '__main__':
  write_file(1, 3, 0.2)
  print(g(2.5))
