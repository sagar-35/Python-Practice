class Student:
    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects
    
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("Subjects: ")
        for subject in self.subjects:
            print(f" - {subject}")
    
    def add_subject(self, new_subject):
        self.subjects.append(new_subject)
        print(f"Subject '{new_subject}' added successfully!")

    def change_name(self, new_name):
        old_name = self.name
        self.name = new_name
        print(f"Name changed from '{old_name}' to '{new_name}'")


s1 = Student("Sagar", 22, ["Python", "Java"])
s1.show_details()

s1.add_subject("English")
s1.change_name("Sagar Hoq")
s1.show_details

s2 = Student("Nila", 20, ["Biology", "Chemistry"])
s2.show_details()

s2.add_subject("Physics")
s2.change_name("Nila Haque")
s2.show_details()

#practice round 
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

b1 = Book("Software QA Automation", "Ahmedul Hoq", 350)

print(b1.title)
print(b1.author)
print(b1.price)
print(b1) #output will be (<__main__.Book object at 0x00000226191B38C0>)

#__str__() functions practice 
class Book1:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Title: {self.title} | Author: {self.author} | Price: {self.price}"

d1 = Book1("Selenium WebDriver", "Sagar Hoq", 500)

print(d1.author)
print(d1.title)
print(d1)


#Methods Objects
class Grade:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def show_grade(self):
        if self.marks >= 80:
            grade = "A+"
        elif self.marks >=70:
            grade = "A"
        elif self.marks >= 50:
            grade = "B"
        else:
            grade = "F"
        print(f"{self.name}'s grade is {grade}")

g1 = Grade("Sagar", 79) # অবজেক্ট তৈরি

g1.show_grade() # মেথড কল করা

# একটা Person নামের ক্লাস তৈরি করা হচ্ছে
class Person:

    # constructor method: object বানানোর সময় name ও age সেট করে
    def __init__(mysillyobj, name, age):
        mysillyobj.name = name # object-এর name property সেট করা
        mysillyobj.age = age # object-এর age property সেট করা

    # একটা method যেটা object-এর তথ্য প্রিন্ট করে
    def show_info(mysillyobj):
        print("Name:",mysillyobj.name)    # object-এর name প্রিন্ট করে
        print("Age :",mysillyobj.age)# object-এর age প্রিন্ট করে

# Person ক্লাস থেকে p1 নামে একটা object বানানো হচ্ছে, name = "Sagar", age = 24
p1 = Person("Sagar", 24)

# object-এর show_info() মেথড কল করা হচ্ছে — name ও age প্রিন্ট করবে
p1.show_info()
        
    