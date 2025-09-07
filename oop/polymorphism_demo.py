import math
class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        ans = self.length * self.width
        return ans 
        
        

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        ans = math.pi * (self.radius** 2)
        return ans