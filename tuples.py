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
