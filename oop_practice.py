class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def is_squre(self):
        return self.length == self.width
        
r1 = Rectangle(2, 30)

print(f"Area: {r1.area()}")

if r1.is_squre:
    print("It's squre.")
else:
    print("It's rectangle, Not squre.")