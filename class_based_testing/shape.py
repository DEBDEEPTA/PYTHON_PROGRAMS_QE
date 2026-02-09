from abc import abstractmethod, ABC
class Shape(ABC):
    def __init__(self,h=None,w=None):
        self.height = h
        self.width = w

    @abstractmethod
    def area(self):
        pass

