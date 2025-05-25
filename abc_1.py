#Vehicle Speed Controller(abstraction)
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_max_speed(self):
        pass

class Car(Vehicle):
    def get_max_speed(self):
        return 180

class Bike(Vehicle):
    def get_max_speed(self):
        return 120

class Truck(Vehicle):
    def get_max_speed(self):
        return 80

vehicles = [Car(), Bike(), Truck()]

for vehicle in vehicles:
    print(f"{vehicle.__class__.__name__} max speed: {vehicle.get_max_speed()}")

        
