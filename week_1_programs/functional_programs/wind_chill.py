import math

t = float(input("Enter temperature in Fahrenheit\n"))
v = float(input("Enter speed in miles/hrs\n"))

CONST_A = 35.74         # CONSTANT NAMING CONVENTION
CONST_B = 0.6225        # CAPITALIZED SNAKE CASE
CONST_C = 0.4275
CONST_D = 35.75
CONST_E = 0.16

w = CONST_A + (CONST_B*t) + (((CONST_C*t)-CONST_D)*math.pow(v,CONST_E))
print(w)