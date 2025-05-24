from abc import ABC, abstractmethod
#abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.1416 * self.radius * self.radius

#object creating and testing

r = Rectangle(5, 10)
c = Circle(7)

print("Rectangle Area: ", r.area())
print("Circle Area: ", c.area())
        
