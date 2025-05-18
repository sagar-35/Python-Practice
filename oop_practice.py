class Employee:
    def __init__(self, name, basic_salary):
        self.name = name 
        self.basic_salary = basic_salary
    
    def calculate_salary(self):
        bonus = self.basic_salary * 0.20 #20% of Basic Salary
        total = self.basic_salary + bonus
        return total
    
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"Salary wiht 20% Bonus: {self.calculate_salary()}")

salary = Employee("Ahmedul Hoq", 50000)
salary.show_info()
        