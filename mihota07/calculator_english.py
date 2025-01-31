import easygui as g
import os
from decimal import *

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == Decimal(0) or b == 0:
        g.msgbox("The second number cannot be zero!")
        return None
    return a / b

def power(a, b):
    return a ** b

def square(a):
    return a ** Decimal(2)

def square_root(a):
    return a ** Decimal(0.5)

def main():
    g.msgbox("Welcome to the calculator!")
    choice = g.choicebox("Please select an operation:", choices=['plus', "minus", "", "division", "square", "square root", "cube", "cube root", 'area', "exit"])
    if choice == "addition":
        a = Decimal(g.enterbox("Please enter the first number:"))
        b = Decimal(g.enterbox("Please enter the second number:"))
        result = add(a, b)
        g.msgbox("The result is: " + str(result))
        os.system('python mihota7.py')
    elif choice == "subtraction":
        a = Decimal(g.enterbox("Please enter the first number:"))
        b = Decimal(g.enterbox("Please enter the second number:"))
        result = subtract(a, b)
        g.msgbox("The result is: " + str(result))
        os.system('python mihota07.py')
    elif choice == "multiplication":
        a = Decimal(g.enterbox("Please enter the first number:"))
        b = Decimal(g.enterbox("Please enter the second number:"))
        result = multiply(a, b)
        g.msgbox("The result is: " + str(result))
        os.system('python mihota07.py')
    elif choice == "division":
        a = Decimal(g.enterbox("Please enter the first number:"))
        b = Decimal(g.enterbox("Please enter the second number:"))
        result = divide(a, b)
        if result is not None:
            g.msgbox("The result is: " + str(result))
            os.system('python mihota07_english.py')
    elif choice == "square":
        a = Decimal(g.enterbox("Please enter a number:"))
        result = square(a)
        g.msgbox("The result is: " + str(result))
        os.system('python mihota07.py')
    elif choice == "square root":
        a = Decimal(g.enterbox("Please enter a number:"))
        result = square_root(a)
        g.msgbox("The result is: " + str(result))
        os.system('python mihota07_english.py')
    elif choice == "cube":
        a = Decimal(g.enterbox("Please enter a number:"))
        result = a ** Decimal(3)
        g.msgbox("The result is: " + str(result))
        os.system('python mihota07_english.py')
    elif choice == "cube root":
        a = Decimal(g.enterbox("Please enter a number:"))
        result = a ** (Decimal(1)/Decimal(3))
        g.msgbox("The result is: " + str(result))
        os.system('python mihota07_english.py')
    elif choice == "exit":
        os.system('python mihota07_english.py')
    elif choice == "area":
        choice1 = g.choicebox("Please select a geometric shape:", choices=["circle", "triangle", "square", "rectangle", "trapezoid", 'exit'])
        if choice1 == "circle":
            a = Decimal(g.enterbox("Please enter the radius of the circle:"))
            result = Decimal(3.14) * a * a
            g.msgbox("The area of the circle is: " + str(result))
            os.system('python mihota07_english.py')
        elif choice1 == "triangle":
            a = Decimal(g.enterbox("Please enter the base of the triangle:"))
            b = Decimal(g.enterbox("Please enter the height of the triangle:"))
            result = Decimal(0.5) * a * b
            g.msgbox("The area of the triangle is: " + str(result))
            os.system('python mihota07_english.py')
        elif choice1 == "square":
            a = Decimal(g.enterbox("Please enter the length of the square:"))
            result = a * a
            g.msgbox("The area of the square is: " + str(result))
            os.system('python mihota07_english.py')
        elif choice1 == "rectangle":
            a = Decimal(g.enterbox("Please enter the length of the rectangle:"))
            b = Decimal(g.enterbox("Please enter the width of the rectangle:"))
            result = a * b
            g.msgbox("The area of the rectangle is: " + str(result))
            os.system('python mihota07_english.py')
        elif choice1 == "trapezoid":
            a = Decimal(g.enterbox("Please enter the upper base of the trapezoid:"))
            b = Decimal(g.enterbox("Please enter the lower base of the trapezoid:"))
            c = Decimal(g.enterbox("Please enter the height of the trapezoid:"))
            result = Decimal(0.5) * (Decimal(a) + Decimal(b)) * Decimal(c)
            g.msgbox("The area of the trapezoid is: " + str(result))
            os.system('python mihota07_english.py')
        elif choice1 == "exit":
            os.system('python mihota07_english.py')


if __name__ == '__main__':
    main()
