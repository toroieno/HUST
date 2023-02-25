# Inverse interpolation - Developed by Le Nguyen Bach - CTTN MI K64

from termcolor        import colored
from math             import *
from sympy            import *
# from customDecorator  import * 

import matplotlib.pyplot as plt
import numpy             as np
import sys 
import time 

EPSILON_SYS   = 1e-15 
EPSILON       = 1e-6
MAXIMUM_POINT = 6 

def setattribute(func): 
    attribute_name = '_attr_' + func.__name__

    @property
    def _wrapper(self):
        if not hasattr(self, attribute_name):
            setattr(self, attribute_name, func(self))  # Create instance attribute.

        return getattr(self, attribute_name)

    return _wrapper


class Inverse_interpolation:
    def __init__(self, table_x, table_y, value_y):
        self.table_x = table_x # Table of x-coordinate of data point(s)
        self.table_y = table_y # Table of y-coordinate of data point(s)
        self.value_y = value_y # y-coordinate of the point we need to approximate

        self.h = table_x[1] - table_x[0] # Jump step

    @classmethod 
    def fromFileInput(cls):
        fileI = open("Input.txt", "r")

        table_x = list(map(float, fileI.readline().split()))
        table_y = list(map(float, fileI.readline().split()))
        value_y = float(fileI.readline())

        fileI.close()
        
        if len(table_x) == 0 or len(table_x) == 1:
            colored("xTableSizeError: xTable doesn't have enough element", 'red')
            sys.exit() 
        
        condition_xJumpStep   = True 
        condition_xIncreasing = True 

        h = table_x[1] - table_x[0]

        for i in range(len(table_x) - 1):
            d = table_x[i + 1] - table_x[i]
        
            if d <= 0:
                condition_xIncreasing = False
                break 
        
            elif abs(d  - h) > EPSILON_SYS:
                condition_xJumpStep = False 
                break  
        
        condition_yTableSize = len(table_y) == len(table_x) 
        condition_yValue     = value_y <= max(*table_y) and value_y >= min(*table_y)  
        
        condition_error = {
            condition_yValue      : f"There are no solution of f(x) = {value_y}",
            condition_yTableSize  : colored(f"TableSizeError: xTable has {len(table_x)} element(s), while yTable has {len(table_y)} element(s)", 'red'),
            condition_xIncreasing : colored("xIncreasingError: xTable must have increasing value from left to right"                           , 'red'),
            condition_xJumpStep   : colored("xJumpStepError: Distance between two consecutive value are not the same"                          , 'red'),
        }.get(False) 
        
        if condition_error == None:
            print(colored("All condition satisfied! Printing the result...", 'yellow'))
        else:
            print(condition_error)
            sys.exit() 
        
        return cls(table_x, table_y, value_y) 
    
    @setattribute
    def __monotonousPartition(self):
        extreme_idx = [0] # Index of all extreme point 
        table_y     = self.table_y 

        for i in range(1, len(table_y) - 1):
            if table_y[i] > max(table_y[i - 1], table_y[i + 1]) or table_y[i] < min(table_y[i - 1], table_y[i + 1]):
                extreme_idx.append(i)
            else:
                continue
        
        extreme_idx.append(len(table_y) - 1)

        mp_idx_list = [] 

        for j in range(len(extreme_idx) - 1):
            index_range = range(extreme_idx[j], extreme_idx[j + 1] + 1)
            mp_idx = [x for x in index_range] # mp is short for "monotonous partition"
            
            mp_idx_list.append(mp_idx) 

        return mp_idx_list

    @setattribute
    def __subMonotonousPartition(self):
        mp_idx_list = self.__monotonousPartition
        table_y     = self.table_y
        value_y     = self.value_y 

        smp_idx_list = [] 
    
        for mp_idx in mp_idx_list:
            # Make sure the par is monotonically increase
            sign = 1 # sign = 1 if monotonically increase, sign = -1 if monotonically decrease
            if table_y[mp_idx[0]] > table_y[mp_idx[1]]:
                sign *= -1 
    
            if value_y > max(table_y[mp_idx[0]], table_y[mp_idx[-1]]) or value_y < min(table_y[mp_idx[0]], table_y[mp_idx[-1]]):
                continue 
    
            # Find the index of two neiboor nearest value of y using binary search
            left_idx  = mp_idx[0]
            right_idx = mp_idx[-1] 
                
            while True:
                idx = int((left_idx + right_idx) / 2) 
                if (value_y - table_y[idx]) * sign > 0:
                    left_idx = idx 
                else: 
                    right_idx = idx 
                        
                if right_idx - left_idx == 1: 
                    break 
    
            # return sub table of y 
            if left_idx + right_idx > mp_idx[0] + mp_idx[-1]:
                right_bound = right_idx 
                left_bound  = max(right_idx - MAXIMUM_POINT + 1, mp_idx[0]) 
                idx_range   = range(left_bound, right_bound + 1)
            
                smp = [i for i in idx_range][::-1] # Short for "sub monotonous partition"
            else:
                left_bound  = left_idx 
                right_bound = min(left_idx + MAXIMUM_POINT - 1, mp_idx[-1])
                idx_range   = range(left_bound, right_bound + 1)
            
                smp = [i for i in idx_range]
    
            smp_idx_list.append(smp)  
    
        return smp_idx_list 
    
    @staticmethod  
    def __add(Mat, new_value):
        if len(Mat[0]) == 0:
            Mat = [[new_value]]
        else:
            new_row       = np.zeros((1, len(Mat)))           # Create a full 0 new row
            new_row[0][0] = new_value                         # Put new_value at left most position of the new row
            Mat           = np.append(new_row, Mat, axis = 0) # Add new row to the top
            new_col       = np.zeros((len(Mat), 1))           # Create a full 0 new column
            Mat           = np.append(Mat, new_col, axis = 1) # Add new column to the right
    
            # Put the correct value(s) to the main diagonal
            for i in range(1, len(Mat)):
                Mat[i][i] = Mat[i - 1][i - 1] - Mat[i][i - 1]
        
        return Mat

    @setattribute 
    def __differenceTable(self): 
        table_y      = self.table_y 
        smp_idx_list = self.__subMonotonousPartition
        dt_list      = []

        for smp_idx in smp_idx_list:
            dt = [[]]
            sub_table_y = [table_y[idx] for idx in smp_idx]

            for y in sub_table_y: 
                dt = self.__add(dt, y)  

            dt_list.append(dt)             
          
        return dt_list  

    @setattribute
    def __yHatT(self):
        dt_list = self.__differenceTable

        yHatT_list = []

        for dt in dt_list:   
            l = len(dt[-1])

            if l == 2:
                yHatT_list.append(0) 
            else:
                yHatT = [[]] # This is yHat, but transpose
    
                for i in range(2, l): 
                    yHatT[0].append(dt[-1][i] / factorial(i)) 

                yHatT_list.append(yHatT)   

        return yHatT_list

    @setattribute 
    def __tHat(self):
        smp_idx_list = self.__subMonotonousPartition
        t            = symbols("t") 

        tHat_list = []
        
        for smp_idx in smp_idx_list:
            l = len(smp_idx) 

            if l == 2:
                tHat_list.append(0)
            else: 
                tHat = [[t**i] for i in range(1, len(smp_idx))] # Or range(1, len(arr) + 1) ??
                tHat_list.append(tHat)

        return tHat_list

    @setattribute
    def __coeff(self):
        sub_idx_list = self.__subMonotonousPartition
        C_list       = []

        for sub_idx in sub_idx_list:
            l = len(sub_idx)

            if l == 2:
                C_list.append(0)
            else:
                C       = np.zeros((l - 2, l - 1)) 
                C[0][0] = -1 
                C[0][1] = 1
                for i in range(1, l - 2):
                    C[i] = np.add(
                        np.roll(C[i - 1], 1), 
                        [-j * (i + 1) for j in C[i - 1]] 
                    )
                
                C_list.append(C)
        
        return C_list 

    @setattribute
    def __phi(self):
        smp_idx_list = self.__subMonotonousPartition
        table_y      = self.table_y 
        t            = symbols("t") 

        yHatT_list = self.__yHatT 
        C_list     = self.__coeff 
        tHat_list  = self.__tHat
        phi_list   = []

        for i in range(len(smp_idx_list)): 
            smp_idx = smp_idx_list[i]
            yHatT   = yHatT_list[i]
            C       = C_list[i] 
            tHat    = tHat_list[i] 

            y0       = table_y[smp_idx[0]]
            delta_y0 = table_y[smp_idx[1]] - y0 
            value_y  = self.value_y 

            phi_expr = (value_y - y0 - (yHatT @ C @ tHat)[0][0]) / delta_y0
            phi_eval = lambdify(t, phi_expr, "math") 
            
            phi_list.append(phi_eval)

        return phi_list

    @setattribute
    def __root(self):
        mono_par = self.__monotonousPartition
        table_x  = self.table_x
        table_y  = self.table_y 
        value_y  = self.value_y 
        h        = self.h

        phi_list     = self.__phi
        smp_idx_list = self.__subMonotonousPartition
         
        root = []

        for i in range(len(mono_par)):
            smp_idx   = smp_idx_list[i]
            phi_eval  = phi_list[i]  

            x0 = table_x[smp_idx[0]]
            y0 = table_y[smp_idx[0]]
            y1 = table_y[smp_idx[1]]

            t0   = (value_y - y0) / (y1 - y0) 
            sign = 1   

            if smp_idx[0] > smp_idx[1]:
                sign *= -1

            count   = 1
            ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10 :: 4]) # Subscript ordinal of a number
            print(colored(f"\nFinding the {ordinal(i + 1)} solution", 'yellow'))
            
            while True:
                temp_t = phi_eval(t0)
                print(f"t_{count} = {temp_t}")

                count += 1
                error  = abs((t0 - temp_t) / t0) 
                t0     = temp_t

                if error < EPSILON:
                    break 

            x = x0 + sign * h * t0   
            root.append(x) 
     
        return root 

    def getResult(self):
        root    = self.__root
        value_y = self.value_y 

        fileO = open("Output.txt", "w")
        fileO.write(f"The set of solutions that satisfied f(x) = {value_y} is {{{', '.join(['{:}'.format(x) for x in root])}}}\n")
        fileO.write("Detail information at the console")

        return None 

def main():
    user = Inverse_interpolation.fromFileInput()
    user.getResult() 

if __name__ == '__main__':
    main()
