### 1 домашка ###
from math import pi

class Circle:
    def __init__(self, r):      # C = 2pR
        self.r = r

    def length(self):
        return 2 * pi * self.r

    def area(self):
        return pi * (self.r ** 2)
circle = Circle(3)
print(circle.area())  
print(circle.length())


### 2 домашка ###
class NotValidFigure(Exception):
    pass

from math import pi

class Circle:
    def __init__(self, r):      # C = 2pR
        self.r = r
        if not self.is_valid():
            raise NotValidFigure

    def length(self):
        return 2 * pi * self.r

    def area(self):
        return pi * (self.r ** 2)

    def is_valid(self):
        if isinstance(self.r,(int, float)):
            return self.r > 0

circle = Circle('dxd')
print(circle.area())  
print(circle.length())
