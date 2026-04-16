# Dars rejasi:
# - Pythonning o'ziga xos jozibasi haqida
# - Numberlarni o'tganamiz
# - String haqida mushohada qilamiz
# - Booleanlarni o'rganamiz

# Python da hammanarsa object, hamma narsa reference ga ega
# Dunder - manosi double under score. __buildins__ dunderi Python ning system variablei hisoblanadi
''' # bular Python ning commentlari
'''
# __buildins__ ning ichki tarkibini kormoqchi bolsak print(dir(__builtins__)) dan yani dir() functioni dan foydalanamiz
# Dunder lar Python ning ichki qurulish mexanizmi

# Dunder __builtins__, __init__
message = "PYTHON: Everything is object!"
print(message)

result = type(message)
print("result:", result)

''' In Python, there are builtin tools:
(1) TYPES > init float str list dict
(2) FUNCTIONS > print() len() input() type() str() int()
(3) CONSTANTS > True False None 
'''

print(dir(__builtins__))
