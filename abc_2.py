#animal sound generator & print a list of animals sound using a loop
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Cow(Animal):
    def make_sound(self):
        return "Cow Sound: Moo!"

class Duck(Animal):
    def make_sound(self):
        return "Duck Sound: Pek Pek."
    
class Lion(Animal):
    def make_sound(self):
        return "Lion sound: Halom!"

animal1 = [Cow (), Duck (), Lion()]
for animal in animal1:
    print(animal.make_sound())