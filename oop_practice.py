class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        return self.celsius * 9/5 + 32
    
    def to_kelvin(self):
        return self.celsius + 273.15

t1 = Temperature(35)
print(f"F = {t1.to_fahrenheit()}")
print(f"K = {t1.to_kelvin()}")
        