''' Array & Set 
    (1) Array
    (2) set
    (3) Specific operators with set
'''
# Python dagi array data type i faqat maxsus holatlarda, katta malumotlar bn ishlashda ishlatilinadi
from array import array
print("----- Array --------")

numbers = array("i", [1, 4, 5, 7, 8, 41])
print("numbers(1):", numbers)

numbers.append(100)
numbers.insert(0, 14)
print("numbers(2):", numbers)

numbers.remove(5)
numbers.pop()
print("numbers(3):", numbers)

del numbers[0:2]
print("numbers(4):", numbers)

print("====== Set =======")
# set of unique collection without keeping order
# set da index bolmaydi va ikki yoki kop marta qayta yozilgan value ni faqat bittasini qabul qiladi

new_numbers = array("i", [1, 4, 5, 7, 5, 4, 7, 8, 4, 41])
numb_set = set(new_numbers)

print(f"the numb_set: {numb_set} and set type: {type(numb_set)}")

numb_set.add(200)  # .add methodi qiymat qo'shadi
print("numb_set(1):", numb_set)

numb_set.add(7)
print("numb_set(2):", numb_set)

print("====== Specifiz operators ======")
# .       | & - ^

a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union. har ikkala to'plamdagi value larni takrorlamasdan faqat bir marta qabul qilib hammasini bit set ga joylab beradi
result2 = a & b  # intersection.  bu bizga intersectionni hosil qilib beradi. har ikkala toplamda berilgan value larni olib beradi
result3 = a - b  # difference   bu operator tafovutni olib beradi. a toplamdan b toplamdagi oxshash value larni ayiradi lekin b toplamdan value a toplamga o'tmaydi
result4 = a ^ b  # symetric difference  ikkala toplamdagi bir xil value larni olib tashlab qolgan value larni bitta set ga joylab beradi

print("print:", result1)
