
class Newton:

    def __init__(self):
        self.arr = []
        self.y = []
        self.a = []
        self.x = []

    def read_file(self, string):
        f = open(string, 'r')
        while True:
            input_str = f.readline()
            if input_str == '':
                break
            arr = input_str.split("\t")
            self.x.append(float(arr[0]))
            self.y.append(float(arr[1]))

        f.close()

    def hoocne_multiply(self, arr):
        b = [1, -arr[0]]
        k = 1
        while k < len(arr):
            b.append(0)
            self.a = [b[0]]  # an = bn
            c = arr[k]
            for i in range(1, len(b)):
                a_k = b[i] - b[i - 1] * c  # a_k = b_k - b_(k + 1) * c
                self.a.append(a_k)
            b = self.a.copy()
            k += 1
        else:
            self.a = b.copy()
        return self.a

    def hoocne_divive(self, arr, c):
        b = [arr[0]]
        for i in range(1, len(arr)):
            b_k = arr[i] + b[i - 1] * c  # b_k = a_k + b_k-1 * c
            b.append(float(b_k))
        return b

    def bangtyhieu(self):
        # khởi tạo mảng hai chiều với phần tử 0
        for i in range(len(self.x)):
            temp_arr = []
            for j in range(len(self.x)):
                temp_arr.append(0)
            self.arr.append(temp_arr)

        # gán giá trị cột đầu tiên là các giá trị y input
        for i in range(len(self.y)):
            self.arr[i][0] = self.y[i]

        # tính các tỷ sai phân
        for col in range(1, len(self.x)):
            for row in range(col, len(self.x)):
                self.arr[row][col] = (self.arr[row][col - 1] - self.arr[row - 1][col - 1]) / (self.x[row] - self.x[row - col])

    def newtonbatky(self):
        # p(x) = y_0
        p = [self.y[0]]
        for i in range(1, len(self.x)):
            # lấy các giá trị của x
            w_array = self.x[0:i]
            # nhân lại trả về 1 mảng là hệ số các phần tử
            w = self.hoocne_multiply(w_array)
            # lấy giá trị bảng sai phân tương ứng
            f = self.arr[i][i]
            # thêm phần tử 0 vào đầu nhằm mục đích cộng các phần từ trong mảng tương ứng
            p.insert(0, 0)
            for j in range(len(w)):
                # nhân với tỉ sai phân tương ứng rồi cộng dồn hệ só
                w[j] *= f
                p[j] += w[j]
        return p

    #tính đạo hàm bậc k của f(x)
    def Degf_k(self, arr, k, c):
        factorial = 1
        for i in range(1, k + 1):
            arr = self.hoocne_divive(arr, c)
            arr.pop()  # lay dao ham nen bo gia tri cuoi di
            factorial *= i
        res = self.hoocne_divive(arr, c).pop()  #lay gia tri tai c
        return factorial * res

    def run(self):
        self.read_file("../input.txt")
        self.bangtyhieu()
        # print(self.newtonbatky())
        print(self.hoocne_divive(self.newtonbatky(), -0.15594603827196885).pop())  #tinh gia tri cua ham tai x0
        print(self.Degf_k(self.newtonbatky(), 1, -0.15594603827196885))  #lay dao ham nham xet tinh bien thien tang hoac giam


if __name__ == '__main__':
    bt = Newton()
    bt.run()