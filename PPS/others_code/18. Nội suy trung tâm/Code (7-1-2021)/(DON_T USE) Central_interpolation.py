# DON'T USE THIS CODE!!! IT'S UGLY AND CONFUSING 

import numpy as np 
import time 

from math import * 

def Above_add(Mat, num):
    new_row = np.zeros((1, len(Mat)))
    new_row[0][0] = num
    Mat = np.append(new_row, Mat, axis = 0)

    Mat = np.append(Mat, np.zeros((len(Mat), 1)), axis = 1)

    for i in range(1, len(Mat)):
        Mat[i][i] = Mat[i-1][i-1] - Mat[i][i-1]

    return Mat 

def Below_add(Mat, num):
    new_row = np.zeros((1, len(Mat)+1))
    new_row[0][0] = num
    for i in range(len(Mat[0])):
        new_row[0][i+1] = Mat[len(Mat)-1][i] - new_row[0][i]

    Mat = np.append(Mat, np.zeros((len(Mat), 1)), axis = 1)

    Mat = np.append(Mat, new_row, axis = 0)

    return Mat  

def Stirling_coef(num):
    S = np.identity(num) 
    for i in range(1, num):
        S[i] = np.add(
            [-x*i*i for x in S[i-1]],
            np.roll(S[i-1], 1)
        )
    return S

def Stirling_interpolation(arr_x, arr_y, x):
    if x > arr_x[len(arr_x) - 1] or x < arr_x[0]:
        print("Giá trị x nằm ngoài khoảng nội suy")
        return None

    h = arr_x[1] - arr_x[0] 
    x0 = round((x - arr_x[0]) / h)
    max_milestone = min(2 * min(len(arr_x) - 1 - x0, x0) + 1, 9) 
    t = (x - arr_x[x0]) / h 
    t_square = t*t
    table = [list(a) for a in zip(arr_x, arr_y)] 
    table = np.roll(table, -x0, axis = 0) 

    T_odd = np.full((max_milestone//2, 1), t)
    for i in range(max_milestone//2 - 1):
        T_odd[i+1][0] = T_odd[i][0]*t_square
    

    T_even = [i*t for i in T_odd]
    
    A_even = [[ ]]
    A_odd = [[ ]]
    del_table = [[table[0][1]]] 
    for i in range(1, max_milestone//2 + 1):
        del_table = Above_add(del_table, table[i][1])
        del_table = Below_add(del_table, table[-i][1])
        l = len(del_table)
        A_odd = np.append(A_odd, [[(del_table[l-2][l-2] + del_table[l-1][l-2])/2/factorial(2*i-1)]], axis = 1)
        A_even = np.append(A_even, [[del_table[l-1][l-1]/factorial(2*i)]], axis = 1)

    S = Stirling_coef(max_milestone // 2)
    value = table[0][1] + np.add(A_even @ S @ T_even, A_odd @ S @ T_odd)[0][0]
    
    error = A_even[0][len(A_even[0])-1]
    for i in range(1, (max_milestone + 1)//2):
        error *= (t_square - i*i)
        
    # print("Ma trận chuyển vị của T_odd\n", np.transpose(T_odd), "\n")
    # print("Ma trận chuyển vị của T_even\n", np.transpose(T_even), "\n")
    # print("Ma trận A_odd\n", A_odd, "\n")
    # print("Ma trận A_even\n", A_even, "\n")
    # print("Bảng sai phân\n", del_table, "\n")
    # print("Ma trận S\n", S, "\n")

    print("Giá trị của f(x) tại x =", x, "là ", value)
    print("Sai số |R(t)| <", abs(error), "\n")
    return value

def Bessel_coef(num):
    B = np.identity(num) 
    for i in range(1, num):
        B[i] = np.add(
            [-x* (i-0.5)**2 for x in B[i-1]],
            np.roll(B[i-1], 1)
        )
    return B
def Bessel_interpolation(arr_x, arr_y, x):
    if x > arr_x[len(arr_x) - 1] or x < arr_x[0]:
        print("Giá trị x nằm ngoài khoảng nội suy")
        return None

    h = arr_x[1] - arr_x[0]
    x0 = int(floor((x - arr_x[0]) / h))
    max_milestone = int(min(2 * min(x0 + 1, len(arr_x) - 1 - x0), 8)) 
    u = (x - arr_x[x0]) / h - 0.5 
    u_square = u*u
    table = [list(a) for a in zip(arr_x, arr_y)] 
    table = np.roll(table, -x0, axis = 0) 

    U_even = np.full((max_milestone//2, 1), 1.0)
    for i in range(max_milestone//2 - 1):
        U_even[i+1][0] = U_even[i][0]*u_square
    
    U_odd = [i*u for i in U_even]
    

    A_even = [[(table[0][1] + table[1][1])/2]]
    del_table = [[table[0][1]]]  
    del_table = Above_add(del_table, table[1][1])
    A_odd = [[del_table[1][1]]]
    for i in range(1, max_milestone//2):
        del_table = Above_add(del_table, table[i+1][1])
        del_table = Below_add(del_table, table[-i][1])
        l = len(del_table)
        A_even = np.append(A_even, [[(del_table[l-2][l-2] + del_table[l-1][l-2])/2/factorial(2*i)]], axis = 1)
        A_odd = np.append(A_odd, [[del_table[l-1][l-1] / factorial(2*i+1)]], axis = 1)
    

    B = Bessel_coef(max_milestone//2)
    print(B)
    value = np.add(A_even @ B @ U_even, A_odd @ B @ U_odd)[0][0] 
    
    error = A_odd[0][len(A_odd[0])-1]
    for i in range(max_milestone//2):
        error *= (u_square - (i+0.5)**2)
        
    # print("Ma trận chuyển vị của U_even\n", np.transpose(U_even), "\n")
    # print("Ma trận chuyển vị của U_odd\n", np.transpose(U_odd), "\n")
    # print("Bảng sai phân\n", del_table, "\n")
    # print("Ma trận hệ số chẵn\n", A_even, "\n")
    # print("Ma trận hệ số lẻ\n", A_odd, "\n")
    # print("Ma trận B\n", B, "\n")
    
    print("Giá trị của f(x) tại x =", x, "là ", value)
    print("Sai số |R(x)| < ", abs(error), "\n")
    return value

start_time = time.time() # Ghi lại thời gian bắt đầu chạy code

arr_x = [0.000, 0.250, 0.500, 0.750, 1.000, 1.250, 1.500, 1.750, 2.000, 2.250, 2.500, 2.750, 3.000]
arr_y = [0.000, 0.074, 0.249, 0.486, 0.745, 1.006, 1.257, 1.493, 1.713, 1.920, 2.112, 2.291, 2.459]
x = 1.274

# Stirling_interpolation(arr_x, arr_y, x)
Bessel_interpolation(arr_x, arr_y, x)

end_time = time.time() # Ghi lại thời gian kết thúc code
print("Total runtime", (end_time - start_time)*1000, "ms")