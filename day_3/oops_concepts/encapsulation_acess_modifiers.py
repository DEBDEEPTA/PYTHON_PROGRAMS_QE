"""
| Modifier  | Syntax   | Meaning
| --------- | -------- | ---------------------------------
| Public    | name   | Accessible everywhere
| Protected | _name  | Accessible in class & subclass
| Private   | __name | Name-mangled (strongly protected)

"""
from enum import nonmember

from day_3.oops_concepts.class_creation import Student


class Bank:
    def __init__(self):
        self.bank_name = "KOTAK"   # public
        self._name = "DEV"
        self.__balance = 10000     # private

    def show(self):
        print(self.__balance)


b = Bank()
print(b.bank_name)   # DIRECT ACESS
# print(b.name)      # No direct acess
                     # Doesn't enforce strict encapsulation
                     # can be acessed as
print(b._name)       # -> b._name

#print(b.balance)        # CANT BE ACESSED DIRECTLY
#print(b._Bank__balance) # Acess through name_mangeling (But Not Good Practice)
b.show()          # using Getter Method (Good Practise)
"""
    Name Mangling Syntax 
         ->  _ClassName__attribute
"""


"""
    GETTERS SETTERS IN PYTHON (GOOD PRACTICSE TO ACESS & MODIFY PRIVATE ATTRIBUTES)
        Approach 1 -> Java Style Aproach
        Approach 2 -> Python Stype (Using
"""

class Student:
    def __init__(self,name=None,age=None):
        self.__name = name
        self.__age = age

    # JAVA STYLE GETTER FOR NAME
    def get_name(self):
        return self.__name
    # JAVA STYLE GETTER FOR AGE
    def get_age(self):
        return self.__age
    # JAVA STYLE SETTER FOR NAME
    def set_name(self,name):
        self.__name = name
    # JAVA STYLE SETTER FOR AGE
    def set_age(self,age):
        self.__age = age


print("Java Style Getter & Setters Example")
s1 = Student()
print(s1.get_name())
print(s1.get_age())

s1.set_name("DEV")
s1.set_age(23)

print(s1.get_name())
print(s1.get_age())

class Employee:
    def __init__(self,name=None,id=None):
        self.__name = name
        self.__id = id

    # PYTHON STYLE GETTER FOR name
    @property
    def name(self):
        return self.__name

    # PYTHON STYLE GETTER FOR id
    @property
    def id(self):
        return  self.__id

    # PYTHON STYLE SETTER FOR name
    @name.setter
    def name(self,name):
        self.__name = name
    # PYTHON STYLE SETTER FOR id
    @id.setter
    def id(self,id):
        self.__id = id

print("Python style Getter & Setter")

e1 = Employee()
print(e1.name)
print(e1.id)
e1.name = "AVI"
e1.id = 32524
print(e1.name)
print(e1.id)

