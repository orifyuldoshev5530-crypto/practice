''' OBJECTS 
    (1) What is object
    (2) Iterable objects & RANGE
    (3) DICTIONATRY
    (4) Error handing system
'''

import array  # package/module
import math  # package
from math import ceil  # method
print("==== What is object ====")
# An object has state and method properties.
# Everything is object in python.

print(type('Hello World'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional programming & OOP
# OOP 4 CONCEPTS > Encapsulation, Abstraction, Inheritance, Polymorphism
result1 = math.ceil(97.7)
print("result1:", result1)

result2 = math.ceil(98.7)
print("result2:", result2)
