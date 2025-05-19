# Doctor Class Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Doctor(Person):
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty
    
    def diagnose(self):
        print(f"Dr. {self.name} is diagnosing a patient as a {self.specialty}")

dr1 = Doctor("Sagar Hoq", 24, "Dentist")
dr1.show_info()
print(f"Specialty: {dr1.specialty}")
dr1.diagnose()