import matplotlib.pyplot as plt
import numpy as np


def add_new_above_point(x, y, arr_x, arr):
    arr_x.insert(0, x)
    temp_arr = [y, arr[0]]
    space = 0
    for i in range(len(arr) + 1):
        space = space + 1
        new_delta = (temp_arr[-1] - temp_arr[-2]) / (arr_x[i] - arr_x[i - space])
        temp_arr.append(new_delta)

    return temp_arr


def add_new_below_point(x, y, arr_x, arr):
    temp_arr = [y]
    space = 0
    for i in range(len(arr) + 1):
        space = space + 1
        new_nabla = (temp_arr[-1] - arr[i]) / (arr_x[i] - arr_x[i - space])
        temp_arr.append(new_nabla)

    return temp_arr


test_arr = [1, 2, 4, 5, 6, 7]
test_arr.insert(0, 8)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
print(test_arr)
print(2.0/(2.0+2.0))
