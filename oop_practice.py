class Circle:

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        pi = 3.1416
        return pi * self.radius ** 2
    
    def perimeter(self):
        pi = 3.1416
        return 2 * pi * self.radius

c1 = Circle(7)

print(f"Area: {c1.area()}")
print(f"Perimete: {c1.perimeter()}")
        