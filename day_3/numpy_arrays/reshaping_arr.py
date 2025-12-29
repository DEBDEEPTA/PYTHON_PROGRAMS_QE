import  numpy as np
from numpy import dtype

arr1 = np.arange(6, dtype=int)
arr2 = arr1.reshape((3,2))

print(arr1) # [1,2,3,4,5]
print(arr2)
"""
    [               -> 3X2 MATRIX
        [0,1]       -> IF ELEMENTS ARE NOT SUFFISIENT FOR THE DESIRE SHAPE
        [2,3]          IT THROW ValueError: can't reshape array
        [4,5]
    ]
"""
