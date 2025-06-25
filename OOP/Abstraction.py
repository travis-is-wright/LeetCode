from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Chicken(Animal):
    def speak(self):
        print("Cluck cluck clooo!")

class Cow(Animal):
    def speak(self):
        print("Mooo Moooo!")

class Dog(Animal):
    def name(self):
        print("Dog")
    def speak(self):
        print("Woof!")

if __name__ == "__main__":
    chicken = Chicken()
    cow = Cow()
    dog = Dog()

    chicken.speak()
    cow.speak()
    dog.name()