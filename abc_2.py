#Employee Salary System(Abstract Class)
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def callculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self):
        self.salary = 50000

    def callculate_salary(self):
        return self.salary 
    
class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours):
        self.hourly_rate = hourly_rate
        self.hours = hours

    def callculate_salary(self):
        return self.hourly_rate * self.hours

#object creating
fulltime = FullTimeEmployee()
parttime = PartTimeEmployee(15, 8)

print(f"Full time salary: {fulltime.callculate_salary()}")
print(f"Part-Time Salary: {parttime.callculate_salary()} Per Day")