class Student:
    collage = "VTU" # <- Class variable (shared by all the objects of the student class)
    def __init__(self,name,age,roll): # <- constructor
        self.name = name  # <- Instance Variable
        self.age =  age
        self.roll = roll

    def __str__(self): # <- Equivalent to java toString() method
                       # <- to return string representation of the object
        return (f"name -> {self.name}\nage -> {self.age}\nroll -> {self.roll}")

    def get_collage(self):
        print(self.collage) # <- to acess class variable use format
                             #    -> ClassName.class_variable_name

s1 =  Student("Dev",22,"CS025")
s2 =  Student("AVI",24,"CS007")
# print(s1)
print(s1.get_collage())
print(s2.get_collage())