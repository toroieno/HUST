# region Input

def read_file(string):
    x = []
    y = []
    f = open(string, 'r')
    while True:
        input_str = f.readline()
        if input_str == '':
            break
        arr = input_str.split(" ")
        x.append(float(arr[0]))
        y.append(float(arr[1]))

    f.close()
    return x, y


# endregion

# region Hoocne


def hoocne_multiply(arr):
    b = [1, -arr[0]]
    k = 1
    while k < len(arr):
        b.append(0)
        a = [b[0]]  # an = bn
        c = arr[k]
        for i in range(1, len(b)):
            a_k = b[i] - b[i - 1] * c  # a_k = b_k - b_(k + 1) * c
            a.append(a_k)
        b = a.copy()
        k += 1
    else:
        a = b.copy()
    return a


def hoocne_divive(arr, c):
    b = [arr[0]]
    for i in range(1, len(arr)):
        b_k = arr[i] + b[i - 1] * c  # b_k = a_k + b_k-1 * c
        b.append(float(b_k))
    return b


# endregion

# region Shared variables

# Dùng cho lagrange và nội suy ngược tính tích
def D_i(arr, i):
    multi = 1
    for k in range(len(arr)):
        if k != i:
            multi *= (arr[i] - arr[k])
    return multi


# Tính tích t(t-1)(t-2)...(dùng trong nội suy ngược)
def multi_t(t, k):
    if k == 0:
        return t
    return multi_t(t, k - 1) * (t - k)


# Tỷ sai phân
def delta_y(arr, begin, end):
    k = end - begin
    if k == 1:
        return arr[end] - arr[begin]
    return delta_y(arr, begin + 1, end) - delta_y(arr, begin, end - 1)


# Đổi biến t
def t(x, x0, h):
    return (x - x0) / h


# endregion

# region Calculation

# Tinh giai thua
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


# Tinh gia tri cua ham so f tai x
def f_x(arr, x):
    return hoocne_divive(arr, x).pop()


# Tính giá trị đạo hàm bậc k của f(x) tai x
def Degf_k(arr, k, x):
    for i in range(1, k + 1):
        arr = hoocne_divive(arr, x)
        arr.pop()  # lay dao ham nen bo gia tri cuoi di
    res = hoocne_divive(arr, x).pop()  # lay gia tri tai x
    return factorial(k) * res

# endregion
