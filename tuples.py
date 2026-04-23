''' TUPLES
  (1) What is the Tuple: typle vs list
  (2) Unpacking arguments
  (3) zip 
'''
# list ni 2 xil usulda qurish mumkin: literal | constructor
# dict va list ham aslida class

# literal
numbs = [3, 5, 1, 4]
car_dict = {"brand": "Ferrari", "year": 1995}
print(numbs)

# constructor
letters = list("Hello world")
person_dict = dict(name="Martin", age=35)
print(letters)


print("------------------------")


##### LIST - qiymatini o'zgartirish mumkin. #########
fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)


#######  TUPLE ######
# we can not mutate tuble
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[2] = "bird" o'zgartirib bolmaydi

# TUPLE VA LIST farqi
# List ichidagi malumotni o'zgartirish, qo'shish mumkin ✅
# Tuple ichidagi malumotni o'chirish, o'zgartirish, qo'shish bolmaydi ❌
# TUPLE ("a", "s")  -  LIST ["a", "s"]
# bazida Tuple larning qavsini yozmasligimiz ham mumkin

# git - "feat: learn tuple and list"

print("----------------- TYPLE (*args) -------------------")
print("======     Unpacking arguments    =======")
# boshqa tillardagi distruction yani qiymatlarni yoyish Python da typle orqali amalga oshiriladi

group = ["MIT", "FELIXY", "DEVEX", "MG"]
(x, y, *z) = group  # *z buyerda x va y dan qolgan "DEVEX" va "MG" qiymatlarini olayapti
print(f"the x: {x} and y: {y}")
print("z:", z)  # list


# *args va **kwargs - qachonki bizga berilayotgan argumentlarning miqdori noaniq bolsa, ishlatilinadi

#  *args > tuple
def calculate(*args):
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


# call
calculate(1, 7, 2, 3)
print("--------")
calculate(0, 2, 300)
print("----------")
calculate(5, 7)


print("-------  **kwargs --------")
# kwargs > dictionary


def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]} years old")


# Call
introduce(name="Justin", age=28)
introduce(name="Shawn", age=30, single=True)
print("----------")


def greeting(*args, **kwargs):
    print("*args:", args)
    print("**kwargs:", kwargs)


# Call
greeting("Hi,", True, 10, name="John", age=22)


print("=====  zip  ======")
tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c')

zipped = zip(tuple1, tuple2)
print("zipped", zipped)
result = list(zipped)
print(f"the result:, {result}")
