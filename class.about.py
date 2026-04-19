''' CLASS
    (1) What is class
    (2) ordinary vs static properties
    (3) special methods
'''

print("==== What is class ====")
# class - temp;ate for object creation
# structure > state constructior method


class Person:
    # state
    message = "static state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do?")

    def say_age(self):
        print(f"{self.name} says: I am {self.age} years old.")

    @classmethod
    def explain(cls):
        print("static method property executed!")


person1 = Person("Justin", 25)
person2 = Person("Alice", 30)
person3 = Person("David", 35)

# ordinary state
print("person1 name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()


print("==== special methods ====")
# Python's most common special methods are below:
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __len__ ...


class Car():
    # state
    description = "This class makes cars"

    # constructor
    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"the {self.name} started the engine!")

    def stop_engine(self):
        print(f"the {self.name} stopped the engine!")

    def __str__(self):
        return f"the {self.name} is a car made in {self.year}"

    def __call__(self):
        print("Object is called as a function!")
        return True


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

print("----")
your_car = Car("Toyota", 2026)
print(your_car)  # __str__ method is called when we print the object
response = your_car()  # __call__ method is called when we call the object as a function
print("response:", response)
