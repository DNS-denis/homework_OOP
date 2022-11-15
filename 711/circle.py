### 1 домашка ###
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**(1/2)

triangle = Triangle(5, 12, 13)
print(triangle.area())



### 2 домашка ###
class NotValidFigure(Exception):
    pass

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not self.is_valid():
            raise NotValidFigure

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**(1/2)

    def is_valid(self):
        sides = [self.a, self.b, self.c]
        if all([isinstance(side,(int, float)) for side in sides]): 
            if all ([side >= 0 for side in sides]):
                if all([side > 0 for side in sides]):
                    sorted_sides = sorted(sides)
                    return sorted_sides[-1] < sorted_sides[0] + sorted_sides[1]

triangle = Triangle(5, 9, 13)
print(triangle.area())
