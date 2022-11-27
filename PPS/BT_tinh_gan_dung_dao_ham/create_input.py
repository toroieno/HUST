from math import *

def g(x):
  # return 3 * x**3 + 2 * x**2 - 3*x + 3
  return 2 * x**2 - 3*x + 3
  # return sin(x)
  # return x**2
  # return 2 * x
 
def write_file(a, b):
  try:
    f = open('input.txt', 'w')
    for i in range(a, b):
      y = g(i)
      f.write("{} {}\n".format(i, y))
  except:
    print('read file error!')
  finally:
    f.close()


if __name__ == '__main__':
  write_file(1,10)
