class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        return self.celsius * 9/5 + 32
    
    def to_kelvin(self):
        return self.celsius + 273.15
    
    def show_result(self):
        print(f"Celsius to Farhenheit: {self.to_fahrenheit()}")
        print(f"Celsius to Kelvin: {self.to_kelvin()}")

t1 = Temperature(35)
t1.show_result()