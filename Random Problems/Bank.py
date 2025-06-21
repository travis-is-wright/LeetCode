class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        return self.__age

p = Person(25)
print(p.age)    # ✅ works, prints 25

p.age = 30

print(p.age)