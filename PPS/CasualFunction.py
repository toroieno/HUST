import numpy as np
import matplotlib.pyplot as plt
from math import *

# region Input

def remove_duplicate_x(arr_x, arr_y):
    temp_arr_x = []
    temp_arr_y = []
    for i in range(len(arr_x)):
        if temp_arr_x.count(arr_x[i]) == 0:
            temp_arr_x.append(arr_x[i])
            temp_arr_y.append(arr_y[i])

    return temp_arr_x, temp_arr_y


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
    return remove_duplicate_x(x, y)


# thêm mốc mới vào phía trên: (x, y): mốc mới; arr_x: các mốc ban đầu; arr: mảng lưu các giá trị tỷ sai phân(đường chéo)
def add_new_above_point(x, y, arr_x, arr):
    arr_x.insert(0, x)
    temp_arr = [y, arr[0]]
    space = 0
    for i in range(len(arr) + 1):
        space = space + 1
        new_delta = (temp_arr[-1] - temp_arr[-2]) / (arr_x[i] - arr_x[i - space])
        temp_arr.append(new_delta)

    return temp_arr


# thêm mốc mới vào phía dưới: (x, y): mốc mới; arr_x: các mốc ban đầu; arr: mảng lưu các giá trị tỷ sai phân(hàng cuối)
def add_new_below_point(x, y, arr_x, arr):
    arr_x.append(x)
    temp_arr = [y]
    space = 0
    for i in range(len(arr) + 1):
        space = space + 1
        new_nabla = (temp_arr[-1] - arr[i]) / (arr_x[i] - arr_x[i - space])
        temp_arr.append(new_nabla)

    return temp_arr


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


def hoocne_divide(arr, c):
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
    return hoocne_divide(arr, x).pop()

# Tính giá trị đạo hàm bậc k của f(x) tai x
def Degf_k(arr, k, x):
    for i in range(1, k + 1):
        arr = hoocne_divide(arr, x)
        arr.pop()  # lay dao ham nen bo gia tri cuoi di
    res = hoocne_divide(arr, x).pop()  # lay gia tri tai x
    return factorial(k) * res


def max_second_derivative(f, a, b, n=1000):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    d2f = np.diff(np.diff(f(x))) / h ** 2
    return np.max(np.abs(d2f))


def max_fourth_derivative(f, a, b, n=1000):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    d4f = np.diff(np.diff(np.diff(np.diff(f(x))))) / h ** 4
    return np.max(np.abs(d4f))

def truy_duoi(A, B, C, d, n):
    alpha = np.empty(n + 1)
    beta = np.empty(n + 1)

    alpha[1] = B[0] / C[0]
    beta[1] = -d[0] / C[0]

    for i in range(1, n):
        alpha[i + 1] = B[i] / (C[i] - alpha[i] * A[i])
        beta[i + 1] = (A[i] * beta[i] + d[i]) / (C[i] - alpha[i] * A[i])

    x = np.empty(n + 1)
    x[n] = (A[n] * beta[n] + d[n]) / (C[n] - A[n] * alpha[n])
    for i in range(n - 1, -1, -1):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]

    return x
# endregion

# region Graph
def draw_graph(x_coeff, p_x, arr_x=None, arr_y=None):
    # draw points
    if arr_x is not None and arr_y is not None:
        x = np.array(arr_x)
        y = np.array(arr_y)
        plt.scatter(x, y, color="red")

    # draw graph
    x_points = np.linspace(x_coeff[0] - 0.5, x_coeff[-1] + 0.5, 1000)
    y_points = [f_x(p_x, x_point) for x_point in x_points]
    plt.plot(x_points, y_points)

    # plt.savefig("mygraph.png")
    plt.show()

# endregion
