class Car: #class   
    def __init__(self, brand, model, year): #constructor method
        self.brand = brand # attributes declear
        self.model = model
        self.year = year
    
    def start_engine(self): # method 
        print(f"{self.brand} {self.model} engine started.")

car1 = Car("Honda", "Civic", 2022)
car2 = Car("BMW", "M6", 2019)

car1.start_engine()

        