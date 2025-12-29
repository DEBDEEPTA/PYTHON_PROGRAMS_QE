"""
| Concept         | Meaning                                         |
| --------------- | ----------------------------------------------- |
| Abstract Class  | A class containing at least one abstract method |
| Abstract Method | A method with no body (implementation)          |

(note) -> In Python, abstract methods exist only inside abstract classes.
       -> You cannot create object of a abstract class
       -> you can't create object of a child class if it doesn't implement's
          the abstract method of the parent class
"""
from abc import abstractmethod
from symtable import Class


class Animal: # <- Abstract class

    @abstractmethod  # <- constructor can be abstract method
    def __init__(self,name):
        pass

    def display_name(self):
        print(self.name)


class Dog(Animal):

    def __init__(self,name=None):
        self.name = name


d1 = Dog("Golden Retrivier")
d2 = Dog()

d1.display_name() # Golden Retriver
d2.display_name() # None


