import numpy as np

def nd_aray_basic():
    """ CREATING A NUMPY ARRAY (ndarray)
        (note) -> ndarray size are fixed
               -> Homogeneous (same data type)
               -> Fixed size
               -> Stored in contiguous memory
               -> Supports negative indexing
               -> Supports slicing
    """
    num_arr = np.array([1, 2, 3, 4, 5])
    print(num_arr)
    print(len(num_arr))

    """
        CREATING ndarray With User Input
        (note) -> For empty() method
                      -> Contains garbage values
                      -> Must be fully overwritten before use
    """

    num_uarr = np.empty(5, dtype=int)  # CREATES A ARRAY OF SIZE 5 WITH INTEGER DATA TYPE
    print(num_uarr)
    print(len(num_arr))

    n = int(input("Enter ndarray size\n"))  # TAKING ARRAY SIZE AS USER INPUT
    num_uarr_ip = np.empty(n, dtype=int)  # DECLEARING ARRAY WIHT INITIAL SIZE & DATA TYPE

    for i in range(n):
        num_uarr_ip[i] = input(f"Enter the element for index {i} -> ")
    print(num_uarr_ip)

    print(f"Element at index [{0}] ->",num_uarr_ip[0])  # ACCESSING ELEMENT BY INDEX
    print("Supports negative Indexing")
    print(f"Element at last index [{-1}] -> ",num_uarr_ip[-1])

def ndarr_props():
    """
        arr.ndim     # number of dimensions
        arr.shape    # tuple of dimensions
        arr.size     # total elements
        arr.dtype    # data type
        arr.itemsize # bytes per element
        arr.nbytes   # Total memory used by the array
    """
    """ ***************** ndim ***********************"""
    """
        CALCULATING NUMBER OF DIMENSIONS
            -> Number of Consecutive opening / closing brackets
        (note)
            -> dimensions size should be Homogeneous
    """
    arr1 = np.array([1,2,3])
    arr2a = np.array([[1,2,3]])
    arr2b = np.array([[1,2,3],[3,4,5],[5,4,6]])
    arr3 = np.array(
        [
            [
                [1,2,3],
                [1,2,3],
                [1,2,3],
                [4,5,6]
            ]
        ]
    )
    print(arr1.ndim)
    """
        (note) -> ndim  # total number of dimensions
               -> len() # Size of the first dimension only
        
    """
    print(arr2a.ndim)
    print(arr2b.ndim)
    print(arr3.ndim)
    """ ***************** shape ***********************"""
    """
        SHAPE IS A TUPLE 
            -> where each value represents the number of elements along a particular axis.
        CALCULATING NUMBER OF DIMENSIONS
            -> array.shape == (axis0_size, axis1_size, axis2_size, ...)
        (note)
            -> Shape should be Homogeneous
    """
    print("Shape Examples")
    arr_a = np.array(
    [ # <-- First Dimension
        [ # <-- 2nd Dimension
            [1,2,3],# <-- 3rd Dimension          # o/p -> (2,2,3)
            [1,2,3],                             # Analogy
                                                 #   -> First Dimensions(List) Consists 2 Dimensions(List)
        ],# <-- 2nd Dimension                    #   -> 2nd Dimensions(List) Consists 2 Dimensions(List)
        [ # <-- 2nd Dimension                    #   -> 3rd Dimesions (as it's the Last dimension) contains 3 elements
            [1,2,3],
            [1,2,3]
        ] # <-- 2nd Dimension
    ] # <-- First Dimension
    )

    print(arr_a.shape)

    """ ***************** size ***********************
        size -> total number of elemments present in the array
    """

    arrs1 = np.array([[1, 2, 3], [3, 4,0], [5,0,0]])
    print(arrs1.size) # -> 9 (total Number Of elements)

    """ ***************** dtype ***********************        
        """
    arrd1 = np.array([[1,2,3],[1,2,3]])
    arrd2 = np.empty(5, dtype=object)
    arrd3 = np.array([[1,2,3.0],
                      [5,3.12,5.343]])
    arrd4 = np.array([["a","b"],
                      ["c", " "]])

    print(arrd1.dtype)   # int64
    print(arrd2.dtype)   # object
    print(arrd3.dtype)   # float64
    print((arrd4.dtype)) # u1 (unsigned 8 bit integer)

    """***************** itemsize *********************** 
        itemsize -> returns size of a element in array
        (note) -> size will be same for all elements as ndarray is homogeneous
    """
    arri1 = np.array([[1,2],
                      [1,2],
                      [1,2]])
    arri2 = np.array(['x','y'])
    print(arri1.itemsize)  # 8  -> bytes (for int)
    print(arri2.itemsize)  # 4  -> bytes (for String)

    """***************** nbytes *********************** 
        nbytes -> returns total memory occupied by the array
        
        CALCULATING TOTAL MEMORY OCCUPIED BY THE ARRAY
               -> (dtype_size x no._of_elements) 
    """
    arrnb1 = np.array([[1, 2],
                      [1, 2],
                      [1, 2]])
    arrnb2 = np.array([
        ['1','2','3'],
        ['1', '2', '3'],
    ])
    print(arrnb1.nbytes) # 48 -> (8x6 = 48)
    print(arrnb2.nbytes) # 24 -> (4X6 = 24)

def main():
    # nd_aray_basic()
     ndarr_props()
if __name__ =="__main__":
    main()


