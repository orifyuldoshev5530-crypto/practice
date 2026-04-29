''' Packages & Debugging 
   (1) Python Packages & Core Packages
   (2) Package Manager & External Package
   (3) Debugging 
'''

# import turtle

# Core package
# t = turtle.Turtle()
# t.shape("Turtle")
# t.speed(2)
# t.circle(150)
# turtle.done()


# Bu kod turtle orqali pizza chizadi
""" import random
from turtle import done, Turtle
print("===== Python Packages & Core Packages =======")
''' Python Packages / Modules: Core, File and External '''
# shu link orqali core package lar royxatini koramiz Core Packages > https://docs.python.org/3/library
# boshqa dasturlash tillarida Package lar library deb ham ataladi


t = Turtle()
t.speed(3)

t.penup()
t.goto(0, -100)
t.pendown()
t.color("orange")
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(0, -90)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(90)
t.end_fill()


for _ in range(15):
    x = random.randint(-60, 60)
    y = random.randint(-60, 60)

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

t.penup()
t.goto(0, 0)
t.pendown()
t.color("black")

for angle in range(0, 360, 45):
    t.setheading(angle)
    t.forward(100)
    t.backward(100)

done()
 """

from PIL import Image
my_file = open("material/massage.txt", "r")
try:
    content = my_file.read()
    print("Content:", content)
finally:
    my_file.close()

# with
with open("material/massage.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("DONE")


print("===== Package Manager & External Package =======")
# Har bir dasturlash tilining o'zini Package manager i bor
''' Package Managers
   Python > pip pipenv
   NodeJS > npm yarn
   PHP > composer
   MacOS > brew 
'''
# External Package > https://pypi.org/

# pillow packagei rasimlar bn ishlashda foydalaniladi


with Image.open("material/logo.png") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")


print("===== Debugging =======")


def get_summary(*args):  # DEFINE
    total_amount = 0
    for a in args:
        total_amount += a
        return total_amount  # find the bug via debugging


test = 100
result = get_summary(1, 2, 3, 4, 5)  # CALL
print("result:", result)
