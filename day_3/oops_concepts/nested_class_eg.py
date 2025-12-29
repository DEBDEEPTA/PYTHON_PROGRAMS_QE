
"""
| Feature                        | Python
| ------------------------------ | -------------------
| Nested class support           | ✅ Yes
| Auto reference to outer object | ❌ No
| Explicit outer object passing  | ✅ Required
| Static inner classes           | All are static-like

 ACCESSING INNER CLASS ->
    syntax -> Level_0_Class.Level_1_Class.Level_2_Class.......Level_N_Class

 ATTRIBUTE LOOKUP NESTED CLASS
    e.g., ->
        class A:     # <- Outer Class (level_0)
            class B: # <- Inner Class (level_1)
                pass
    lookup ->
            A.B.attribute_name

"""

class Collage:
    collage_name = "VTU"
    class Studnent:
        def __init__(self,name,age):
            self.name = name
            self.age = age

        def display_student(self):
            print(self.name)
            print(self.age)

        def display_collage(self):
            print(Collage.collage_name)

s1 = Collage.Studnent("dev",23)
s2 = Collage.Studnent('Avi',25)
print("Student 1 Details")
s1.display_student()
s1.display_collage()
print("Student 2 Details")
s2.display_student()
s2.display_collage()