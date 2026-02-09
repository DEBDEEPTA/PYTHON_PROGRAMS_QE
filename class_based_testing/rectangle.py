from class_based_testing.shape import Shape


class Rectangle(Shape):
    def __init__(self,h,w):
        super().__init__(h,w)

    def area(self):
        val =  int(self.height * self.width)
        return val