import math

from class_based_testing.shape import Shape

class Circle(Shape):
    PI_VAL = math.pi
    def __init__(self,r):
        self.radius = r

    def area(self):
        val = int(Circle.PI_VAL * (math.pow(self.radius,2)))
        return val
