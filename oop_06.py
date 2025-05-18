class Person: # Parent Class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    
class Student(Person): # child class: Student
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def show_student(self):
        self.show_info()
        print(f"Student ID: {self.student_id}")
    
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def show_teacher(self):
        self.show_info()
        print(f"Teacher's Subject is: {self.subject}")

s1 = Student("Sagar", 22, 525)
s2 = Student("Sam", 23, 524)
s3 = Student("Rayhan", 25, 504)
s1.show_student()
s2.show_info()

t1 = Teacher("MD Touhid", 35, "Information System Security")
t1.show_info()
t1.show_teacher()