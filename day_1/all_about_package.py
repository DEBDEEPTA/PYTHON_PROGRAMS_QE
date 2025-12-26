
# import example_package
# import example_package as eg
# import example_package.example_sub_package

"""
    RELATIVE IMPORTING (ONLY WORKS WITH PACKAGE PRESENT IN THE SAME DICRECTORY)

"""
import example_package.example_sub_package; # RELATIVE IMPORTING

"""
    ABSOLUTE IMPORTING (RECOMMENDED) 
"""
from day_1.example_package.example_sub_package import eg_func # ABSOLUTE IMORTING

print(eg_func.add_nums(10,20,30))
print(eg_func.mul_nums(10,20,30))

"""
    USING ALIASED IMPORT NAME
"""
from day_1.example_package.example_sub_package import eg_func as my_func
print(my_func.add_nums(1,2,3))
print(my_func.add_nums(1,2,3))

"""
    IMPORTING THE FUNCTION OF THE FILE DIRECTLY 
"""
from day_1.example_package.example_sub_package.eg_func import add_nums as add
from day_1.example_package.example_sub_package.eg_func import mul_nums as mul
print(add(7,8,9))
print(mul(7,8,9))