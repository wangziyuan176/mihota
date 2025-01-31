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
        g.msgbox("不可以除以0！")
        return None
    return a / b
def power(a, b):
    return a ** b
def square(a):
    return a ** Decimal(2)
def square_root(a):
    return a ** Decimal(0.5)
def main():
    g.msgbox("欢迎使用计算器！")
    choice = g.choicebox("请选择操作：", choices=["加法", "减法", "乘法", "除法", "平方", "平方根", "立方", "立方根",'面积',"退出"])
    if choice == "加法":
        a = Decimal(g.enterbox("请输入第一个数字："))
        b = Decimal(g.enterbox("请输入第二个数字："))
        result = add(a, b)
        g.msgbox("结果为：" + str(result))
        os.system('python mihota07.py')
    elif choice == "减法":
        a = Decimal(g.enterbox("请输入第一个数字："))
        b = Decimal(g.enterbox("请输入第二个数字："))
        result = subtract(a, b)
        g.msgbox("结果为：" + str(result))
        os.system('python mihota07.py')
    elif choice == "乘法":
        a = Decimal(g.enterbox("请输入第一个数字："))
        b = Decimal(g.enterbox("请输入第二个数字："))
        result = multiply(a, b)
        g.msgbox("结果为：" + str(result))
        os.system('python mihota06.py')
    elif choice == "除法":
        a = Decimal(g.enterbox("请输入第一个数字："))
        b = Decimal(g.enterbox("请输入第二个数字："))
        result = divide(a, b)
        if result is not None:
            g.msgbox("结果为：" + str(result))
            os.system('python mihota07.py')
    elif choice == "平方":
        a = Decimal(g.enterbox("请输入一个数字："))
        result = square(a)
        g.msgbox("结果为：" + str(result))
        os.system('python mihota07.py')
    elif choice == "平方根":
        a = Decimal(g.enterbox("请输入一个数字："))
        result = square_root(a)
        g.msgbox("结果为：" + str(result))
        os.system('python mihota07.py')
    elif choice == "立方":
        a = Decimal(g.enterbox("请输入一个数字："))
        result = a ** Decimal(3)
        g.msgbox("结果为：" + str(result))
        os.system('python mihota07.py')
    elif choice == "立方根":
        a = Decimal(g.enterbox("请输入一个数字："))
        result = a ** (Decimal(1)/Decimal(3))
        g.msgbox("结果为：" + str(result))
        os.system('python mihota07.py')
    elif choice == "退出":
        os.system('python mihota07.py')
    elif choice == "面积":
        choice1=g.choicebox("请选择几何图形：",choices=["圆形","三角形","正方形","长方形","梯形",'退出'])
        if choice1=="圆形":
            a=Decimal(g.enterbox("请输入圆的半径："))
            result=Decimal(3.14)*a*a
            g.msgbox("圆的面积为："+str(result))
            os.system('python mihota07.py')
        elif choice1=="三角形":
            a=Decimal(g.enterbox("请输入三角形的底："))
            b=Decimal(g.enterbox("请输入三角形的高："))
            result=Decimal(0.5)*a*b
            g.msgbox("三角形的面积为："+str(result))
            os.system('python mihota07.py')
        elif choice1=="正方形":
            a=Decimal(g.enterbox("请输入正方形的边长："))
            result=a*a
            g.msgbox("正方形的面积为："+str(result))
            os.system('python mihota07.py')
        elif choice1=="长方形":
            a=Decimal(g.enterbox("请输入长方形的长："))
            b=Decimal(g.enterbox("请输入长方形的宽："))
            result=a*b
            g.msgbox("长方形的面积为："+str(result))
            os.system('python mihota07.py')
        elif choice1=="梯形":
            a=Decimal(g.enterbox("请输入梯形的上底："))
            b=Decimal(g.enterbox("请输入梯形的下底："))
            c=Decimal(g.enterbox("请输入梯形的高："))
            result=Decimal(0.5)*(Decimal(a)+Decimal(b))*Decimal(c)
            g.msgbox("梯形的面积为："+str(result))
            os.system('python mihota07.py')
        elif choice1=="退出":
            os.system('python mihota07.py')


if __name__ == '__main__':
    main()
