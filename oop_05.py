class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def calculate_average(self):
        return sum(self.marks) / len(self.marks)
    
    def is_passed(self):
        for mark in self.marks:
            if mark < 40:
                return False
        return True
    
    def show_result(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.calculate_average()}")
        if self.is_passed():
            print("Status Passed.")
        else:
            print("Status Not Passed!")

a1 = Student("Sagar", [3, 12])

a1.show_result()
