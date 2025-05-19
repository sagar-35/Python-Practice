class Vehicle:
    def __init__(self, brand, year): #attributes
        self.brand = brand
        self.year = year

    def show_info(self):
        print(f"{self.brand} {self.year} engine is ok.")

class Car(Vehicle): #child class
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
    
    def drive(self):
        print(f"The {self.brand} {self.model} is now driving.")

car1 = Car("BMW", 2022, "I8")

car1.show_info()
print(f"Model: {car1.model}")
car1.drive()
            