import  numpy as np
from numpy import dtype

arr1 = np.arange(1,13,1, dtype=int)
arr2 = arr1.reshape((2,2,3))    # (2,2,3) --> total 2*2*3 = 12 elements should be present in the array which we want to reshape

print(arr1) # [1,2,3,4,5]
print(arr2)
"""
    [               -> 3X2 MATRIX
        [0,1]       -> IF ELEMENTS ARE NOT SUFFISIENT FOR THE DESIRE SHAPE
        [2,3]          IT THROW ValueError: can't reshape array
        [4,5]
    ]
"""
