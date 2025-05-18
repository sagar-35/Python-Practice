class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")
    
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
    
    def drive(self):
        print(f"The {self.brand} {self.model} is now driving")

c1 = Car("Mercedse", 2022, "Benz")
c1.show_info()
print(f"Model: {c1.model}")
c1.drive()    