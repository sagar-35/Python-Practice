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