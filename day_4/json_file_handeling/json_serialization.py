"""
    9. JSON Serialization Limitations (Special Cases)
    ❌ JSON cannot store
        -> set
        -> tuple
        -> datetime
        -> custom objects
"""
from Scripts.unicodedata import name
import  json

class Studnet:
    def __init__(self,name=None,age=None):
        self.__name = name
        self.__age = age

    # GETTERS
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    # SETTERS
    @name.setter
    def name(self,name):
        self.__name = name
    @age.setter
    def age(self,age):
        self.__age = age

    def __str__(self):
        return f"{self.name} ---> {self.age}"

s1 = Studnet()
s2 = Studnet("Dev",23)

json_string = json.dumps(s2.__dict__) # ALL INSTANCE VARIABLES OF THE object STORED IN A DICTIONARY --> object_name.__dict__
print(json_string)
print(type(json_string))

json_object = json.loads(json_string)

print(json_object)
print(type(json_object))
print(json_object["_Studnet__name"])