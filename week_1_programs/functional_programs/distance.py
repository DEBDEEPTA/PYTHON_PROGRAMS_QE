"""
3.  Writeaprogram Distance.java that takes two integer command-line arguments x
    and y and prints the Euclidean distance from the point (x,y) to the origin(0,0).The
    formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
"""
import math

x_value = int(input("enter x value\n"))
y_value = int(input("enter y value\n"))
print(math.sqrt( math.pow(x_value,2) + math.pow(y_value,2) ))