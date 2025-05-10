class Student:
    def __init__(self, name, age):
        self.name = name #obejct's name attribute set
        self.age = age #object's age attribute set

#making object
s1 = Student("Sagar", 22)
s2 = Student("Nila", 21)

#print
print(s1.age)
print(s2.name)


#Car Class practice
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

#Object making
c1 = Car("Honda", "Civic", 2022)
c2 = Car("Toyota", "Voxy", 2018)
c3 = Car("Honda", "Grace", 2017)

#print
print(c1.model)
print(c2.brand)
print(c3.year)
print(f"Brand: {c1.brand} | Model: {c1.model} | Year: {c1.year}")
        

#Show_Details

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

m1 = Student("Hasan", 22, ["Python", "Math", "English"])
m1.show_details()


#auto __init__() how __init__ method works
        
class Example:
    def __init__(self):
        print("init cholteche")
    
    def hello(self):
        print("ami hello method")

obj = Example()
obj.hello()
        


