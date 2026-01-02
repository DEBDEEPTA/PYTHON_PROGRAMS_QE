# NUMPY_HANDBOOK 

| PYTHON LIST                   | NUMPY                                       |
|-------------------------------|---------------------------------------------|
| Slow for large numerical data | ndarray (N-dimensional array)               |
| Memory-inefficient            | Vectorized operations (fast, C-level speed) |
| Lack mathematical operations  | Linear algebra, statistics, random sampling |
|                               | Foundation for Pandas, SciPy, ML, DL        |

### 1. Installing & Importing NumPy
```
pip install numpy
import numpy as np
```
### 2. ndarray
| characteristics                         |
|-----------------------------------------|
| Homogeneous (same data type)            |
| Fixed size                              |
| Stored in contiguous memory             |
| Supports negative indexing              |
| Supports slicing -> _[start,stop,step]_ |

1. _Creating A Numpy Array_
    ```
   import numpy as np
   arr = np.array([1, 2, 3, 4])
   print(arr)
   ```
2. _Key Properties_
    ```
    arr.ndim     # number of dimensions
    arr.shape    # tuple of dimensions
    arr.size     # total elements
    arr.dtype    # data type
    arr.itemsize # bytes per element
    arr.nbytes   # total memory used by the array
   ```
3. _Inbuild Array Creation Functions_
   ```
   np.zeros((2,3))    # filled all positons with 0
   np.ones((3,3))     # filled all positions with 1
   np.eye(3)          # Identity matrix (only digonal elements = 1, else 0)
   np.arange(0,10,2)  # syntax -> np.arange(start, stop, step, dtype=None)
                               -> [0,2,4,6,8]
   np.linspace(0,1,5) # creates a fixed number of evenly spaced values between two limits.
                      # syntax -> np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
                               -> [0. 0.5 0.5 0.75  1.]
   np.empty((2, 2))   # create 2x2 empety matrix (contains garbadge values)
   np.full((3, 3), 7) # fill with specific value

   ```
4. _Reshaping Arrays_
   ```
   import  numpy as np
   from numpy import dtype

   arr1 = np.arange(6, dtype=int) 
   arr2 = arr1.reshape((3,2))

   print(arr1) # [0,2,3,4,5]
   print(arr2)
   """
    [               -> 3X2 MATRIX
        [0,1]       -> IF ELEMENTS ARE NOT SUFFISIENT FOR THE DESIRE SHAPE
        [2,3]          IT THROW ValueError: can't reshape array
        [4,5]
    ]
   """

   ```
5. _Vectorization & Universal Functions_ 
   ```
   Vectorization
    -> Performing operations on entire arrays (vectors/matrices) at once, without explicit Python loops.
   a = np.array([1, 2, 3])
   b = np.array([4, 5, 6])

   print(a + b)      # [5 7 9]
   print(a * b)     # [ 4 10 18]
   print(a ** 2)     # [1 4 9]

| Universal Function | Example       |
|--------------------| ------------- |
| `np.sqrt`          | square root   |
| `np.log`           | natural log   |
| `np.exp`           | exponential   |
| `np.sin`           | trigonometric |
| `np.abs`           | absolute      |

   ```
