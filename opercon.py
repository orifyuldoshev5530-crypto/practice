''' OPERATORS & CONDITIONS
    (1) Oprators
    (2) Conditions
    (3) Logical Operators
'''
print("==== Operators ====")

# + - > >= > == /  // % += **

a = 19
b = 5

print("a + b", a + b)
print("a * b", a * b)
print("a / b", a / b)

print("------------")

result = a // b  # natijani yaxlitlaydi. 3.8 ni 3 ga yaxlitlaydi 4 ga emas
left = a % b  # qoldiqni chiqaradi. 19 ni 5 ga bo'lganda 4 qoldiq qoladi
print(f" the result {result} and the left {left}")

# a = a * 100
a += 100
print("a:", a)

print("b**2", b**2)  # b ni kvadratini chiqaradi. 5 ni 2 ga ko'paytiradi. 5*5=25
print("b**3", b**3)  # b ni kubini chiqaradi. b*b*b

print("=" * 5)  # Pythonda stringlarni ham kopaytirish mumkin

# == belgilar orqali Node.js da objectlarni solishtirsa, unda reference solishtiriladi. Pythonda esa faqat qiymatlar solishtiriladi

c = dict(name="Martin", age=30)
d = dict(name="Martin", age=30)
e = c

print("c == d", c == d)  # True chunki qiymatlar teng

# Objectlarimiz bitta referencega egaligini is operatori orqali tekshiramiz
print("c is d", c is d)  # False chunki c va d alohida referencelarga ega
print("c is e", c is e)  # True chunki referense bitta
print(id(c), id(d))

# Value larni tekshirmoqchi bo'lsak -  ==
# Reference larni tekshirmoqchi bo'lsak - is
print("==== Conditions ====")
