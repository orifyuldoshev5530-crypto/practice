''' FUNCTIONS
(1) Define vs Call
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope
'''
# None = Undefined
# Pythonda function qurilganda u bo'sh qolmasligi kk, hech bolmaganda pass sintaksisi yozilishi kk

print("==== Define vs Call ====")
# build in function > print() type()
# Function - reusable block of code!
# Instead of block {} in JAVA, Python uses indentation!

# DEFINE - build


def greet(a):
    print(f"How do you do, {a}")  # void function


def greeting(b):
    print("greeting is executed")  # return function
    return f"Hi, {b}"


# CALL - execute
result1 = greet("Martin")
print("result1:", result1)  # Void F call

result2 = greeting("Justin")  # Return F call
print("result2:", result2)
