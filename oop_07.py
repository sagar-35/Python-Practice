class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Bike(Vehicle):
    def move(self):
        print("Riding!")

bike1 = Bike()
bike1.move()
        