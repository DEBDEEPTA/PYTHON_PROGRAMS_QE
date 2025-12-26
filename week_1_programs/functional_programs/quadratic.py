"""
     Write a program Quadratic.java to find the roots of the equation a*x*x+b*x+c.
    Since the equation is x*x,hence there are 2 roots.The 2 roots of the equation
    can be found using a formula (Note: Take a, b and c as input values)
    delta = b*b - 4*a*c
    Root 1 of x = (-b + sqrt(delta))/(2*a)
    Root 2 of x = (-b - sqrt(delta))/(2*a)
"""
import math
from difflib import Match

a = int(input("enter value of a\n"))
b = int(input("enter value of b\n"))
c = int(input("enter value of c\n"))

delta= ((b**2) - (4*a*c))

r1,r2 = 0,0
if delta > 0:
    r1 = ((-b + math.sqrt(delta)) / (2 * a))
    r2 = ((-b - math.sqrt(delta)) / (2 * a))
    print(f"Root 1 of x = {r1}")
    print(f"Root 2 of x = {r2}")
elif delta == 0:
    r = -b /(2*a)
    print(f"Root of x = {r}")
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-delta) / (2 * a)
    print("Two complex roots:")
    print(f"Root 1 = {real_part} + {imaginary_part:.2f}i")
    print(f"Root 2 = {real_part} - {imaginary_part:.2f}i")

