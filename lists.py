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
