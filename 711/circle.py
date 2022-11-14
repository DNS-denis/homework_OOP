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
        sides = [self.r]
        if all([isinstance(side,(int, float)) for side in sides]):
            if all ([side >= 0 for side in sides]):
                return all([side > 0 for side in sides])

circle = Circle(-3)
print(circle.area())  
print(circle.length())