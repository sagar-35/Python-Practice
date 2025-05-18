class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
    
class Doctor(Employee):
    def __init__(self, name, salary, specialization):
        super().__init__(name, salary)
        self.speacialization = specialization
    
    def treat_patient(self):
        print(f"Dr. {self.name} is now treating a patient")
    
d1 = Doctor("Jaman DJ", 90000, "Cardologist")
d1.show_info()
print(f"Speacialization: {d1.speacialization}")
d1.treat_patient()