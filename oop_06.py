#Employee & Manager
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def manage(self):
        print("Manager of the IT department is managing the QA team.")

mng1 = Manager("Sagar Hoq", 50000, "Software Quality Assurance Team")

mng1.show_info()
print(f"Department: {mng1.department}")
mng1.manage()