''' List
    (1) List methods
    (2) Lambda function
    (4) enumarate, map and filter
'''

print("===== Working with lists =====")
# Java/PHP/Node.js dagi array => Python da list deyiladi

# literal
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Michail")  # tuple
groups = ["MIT", "FELIXY", "DEVEX", "MG"]  # list
for team in groups:
    print(f"the team: {team}")


# constructor
letters = list("Hello World")
print(f"the letters: {letters} and size {len(letters)}")


print("-------------------")

fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
# 0 chi qiymatdan 2 chi qiymatgacha bolgan value larni olib ber degani
b = fruits[0:2]
c = fruits[::3]  # 0 chi qiymatdan 3 qadam sakra degani
d = fruits[::-1]  # value larni teskari qilib olib beradi

print("a", a)
print("b", b)
print("c", c)
print("d", d)


print("========  List methods ========")
# mutable methods => append() insert() pop() remove() clear() sort()
# immutable methods => sorted() index()

letters = ["a", "b", "k"]

letters.append("c")  # add behind
print(f"the append letters: {letters}")

# add font  doim qo'shmoqchi bolgan argumentimizning joylashish indexini ko'rsarishimiz kerak
letters.insert(0, "z")
print(f"the insert letters: {letters}")

size = len(letters)  # size = len(letters) -1   qilsa ham boladi
# pop behind.  pop - list dan value larni olib beradi
result1 = letters.pop(size - 1)
print(f"the pop result: {result1} and letters: {letters}")

result2 = letters.pop(0)  # pop font
print(f"the pop result2: {result2} and letters: {letters}")


print("--------------")

animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")  # ko'rsatilgan valueni olib tashlaydi
print("animals remove:", animals)

del animals[2:4]  # ko'rsatilgan value ni delete qiladi
print("animals delete:", animals)

exist = animals.index("cat")  # listdagi value larning indexini aniqlab beradi
print("cat exist:", exist)

animals.clear()  # list dagi value larni o'chirib yuboradi
print("animals clear:", animals)

if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")

print("-----------------")
numbers = [2, 20, 12, 8, 57]
numbers.sort()  # value larni tartiblab beradi
print("sort default:", numbers)
# value larni teskari yani katta raqamlardan boshlab tartiblab beradi
numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutable sorted
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)  # immutable holatda sort qilib beradi
print(f"the sorted numbs {numbs} and nuw_numbs: {new_numbs}")


print("------------ Lambda function ------------")
# lamda is small anonimous function
def calculate(x, y): return x * y


result = calculate(3, 5)
print("result:", result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30),
    ("Ali", 41),
]
people.sort()
print("people(1)", people)

# sort by age via lambda
people.sort(key=lambda people: people[1])
print("people(2)", people)


print("======== enumerate map and filter ==========")
# enumerate for index & value
# enumerate listdagi value larning  index va value larini qabul qilish uchun ishlatilinadi

animals = ["dog", "cat", "fish"]  # list
for element in enumerate(animals):
    print("element:", element)

for (index, value) in enumerate(animals):
    print(f"the index: {index} and value: {value}")

print("-------------------")
# similar in dictionaries
car_obj = dict(brand="Ferrari", year=2023)  # dict
result = car_obj.items()  # dict dagi value larni tuple qilib yoyib beradi
for (key, value) in result:
    print(f"the key: {key} and value: {value}")

print("-----------------")
# map
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33),
]

result_map = map(lambda car: car[0], cars)
print(f"the result_map: {result_map} and type: {type(result_map)}")
new_cars = list(result_map)
print("new_cars", new_cars)

print("----------------------")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(f"the result_filter: {result_filter} and type: {type(result_filter)}")
print(list(result_filter))
print(cars)
