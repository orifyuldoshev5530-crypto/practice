''' CLASS deep dive
    (1) ENCAPSULATION
    (2) INHERITENCE
    (3) POLIMORPHISM
'''

print("==== INHERITENCE ====")
# PARENT > CHILD
# Parent providesonly public & protected properties(state + method)


class Animal:
    description = "The class makes animals"

    def __init__(self, voice):
        self.voice = voice

    # method
    def make_voice(self):
        print("the animal can make voice:", self.voice)


class Dog(Animal):  # child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        super().__init__(voice)  # parent constructorini chaqiramiz
        self.name = name
        self.sound = sound

    # method
    def introduce(self):
        print(f"{self.name} says {self.sound}-{self.sound}")

    def make_voice(self):
        print("Yes, I can protected you!")

    def make_voice(self):
        print(f"the {self.name} can make voice:", self.sound)


class Cat(Animal):

    # constructor
    def __init__(self, name, sound, voice):
        super().__init__(voice)  # parent constructorini chaqiramiz
        self.name = name
        self.sound = sound

    # method
    def introduce(self):
        print(f"{self.name} says {self.sound}-{self.sound}")

    def make_voice(self):
        pass


class Fish(Animal):

    # constructor
    def __init__(self, name, sound, voice):
        super().__init__(voice)  # parent constructorini chaqiramiz
        self.name = name
        self.sound = sound

    # method
    def introduce(self):
        print(f"{self.name} says {self.sound}-{self.sound}")

    def make_voice(self):
        pass


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "meow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("------------")
dog.make_voice()
fish.make_voice()

# print(Animal.description)
# print("dog.status:", dog._status)
# print("cat.status:", cat._status)

print("==== POLIMORPHISM ====")
# Polimorphism > the same method can have different implementations in different classes

dog.make_voice()
cat.make_voice()

print("------------")
# fish > Fish > Animal > object
a = isinstance(fish, Fish)  # True
b = isinstance(fish, Animal)  # True
c = isinstance(fish, object)  # True
d = isinstance("MIT", object)  # True
result = a and b and c and d
print(f"the result: {result}")

# Fish > Animal > object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data:", data1, data2)
