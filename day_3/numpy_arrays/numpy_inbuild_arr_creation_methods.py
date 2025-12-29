""" standard inbuild predefined array creations methods
        ->
 """
from numpy import dtype

"""******************* zeros() **********************
    syntax -> zeros((axis1_size,axis2_size,........no._of_elements_in_last_axis), dtype = value)
"""
import numpy as np
arrz1 = np.zeros(5)
arrz2 =np.zeros((2, 3), dtype=int)

print(arrz1)
print(arrz1.dtype)

print(arrz2)
print(arrz2.dtype)

"""
   ******************* ones() **********************
    syntax -> zeros((axis1_size,axis2_size,........no._of_elements_in_last_axis), dtype = value)
"""

arr11 = np.ones(5)
arr12 = np.ones((3,3,2), dtype=int)
print(arr11)
print(arr11.dtype)
print(arr12)
print(arr12.dtype)
"""
   ******************* eye() **********************
"""
print("Identity Matrix")
arrey1 = np.eye(3,2) # identity matrix of 3x2  of float(defalult upcasting for numeric value)
arrey2 = np.eye(5, dtype=int) # Identity matrix of 5x5 of integer
print(arrey1)
print(arrey1.dtype)

print(arrey2)
print(arrey2.dtype)

"""**************************full()***********************"""
arrf1 = np.full((3, 2), 7,dtype=int) # 3x2 Matrix filled with 7
arrf2 = np.full(5, 3.14)   # 5x1 matrix filled with 3.14
print(arrf1)
print(arrf2)

arrls1 = np.linspace(0,1,5)
print(arrls1)