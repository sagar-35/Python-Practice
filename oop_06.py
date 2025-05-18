class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("Some generic animal sound")
    
class Cat(Animal):
    def make_sound(self):
        print(f"{self.name}'s sound Meow")

class Cow(Animal):
    def make_sound(self):
        print(f"{self.name}'s sound Moo")
a1 = Animal("Some Animal")
a1.make_sound()


c1 = Cat("Cat")
c1.make_sound()

c2 = Cow("Cow")
c2.make_sound()