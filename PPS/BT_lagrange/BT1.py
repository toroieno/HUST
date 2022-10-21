class Lagrange:
  def read_file(self):
    try:
      f = open("input.txt", "r")
      self.x = []
      self.y = []
      all_arr = f.read().split("\n")
      print(all_arr)
      for each in all_arr:
        arr = each.split(" ")
        self.x.append(arr[0])
        self.y.append(arr[1])
    except:
      print('Open file error!')
    finally:
      f.close()
  
  def lagrange(self):
    print(self.x)
    print(self.y)

  #main
  def run(self):
    self.read_file()
    self.lagrange()

#--------------------main--------------------
bt = Lagrange()
bt.run()