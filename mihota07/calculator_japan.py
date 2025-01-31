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
        g.msgbox("ゼロで割ることはできません！")
        return None
    return a / b

def power(a, b):
    return a ** b

def square(a):
    return a ** Decimal(2)

def square_root(a):
    return a ** Decimal(0.5)

def main():
    g.msgbox("計算機をご利用いただきありがとうございます！")
    choice = g.choicebox("操作を選択してください：", choices=["足し算", "引き算", "掛け算", "割り算", "二乗", "平方根", "立方", "立方根", '面積', "終了"])
    if choice == "足し算":
        a = Decimal(g.enterbox("最初の数字を入力してください："))
        b = Decimal(g.enterbox("二番目の数字を入力してください："))
        result = add(a, b)
        g.msgbox("結果は：" + str(result))
        os.system('python mihota07_japan.py')
    elif choice == "引き算":
        a = Decimal(g.enterbox("最初の数字を入力してください："))
        b = Decimal(g.enterbox("二番目の数字を入力してください："))
        result = subtract(a, b)
        g.msgbox("結果は：" + str(result))
        os.system('python mihota07_japan.py')
    elif choice == "掛け算":
        a = Decimal(g.enterbox("最初の数字を入力してください："))
        b = Decimal(g.enterbox("二番目の数字を入力してください："))
        result = multiply(a, b)
        g.msgbox("結果は：" + str(result))
        os.system('python mihota07_japan.py')
    elif choice == "割り算":
        a = Decimal(g.enterbox("最初の数字を入力してください："))
        b = Decimal(g.enterbox("二番目の数字を入力してください："))
        result = divide(a, b)
        if result is not None:
            g.msgbox("結果は：" + str(result))
            os.system('python mihota07_japan.py')
    elif choice == "二乗":
        a = Decimal(g.enterbox("数字を入力してください："))
        result = square(a)
        g.msgbox("結果は：" + str(result))
        os.system('python mihota07_japan.py')
    elif choice == "平方根":
        a = Decimal(g.enterbox("数字を入力してください："))
        result = square_root(a)
        g.msgbox("結果は：" + str(result))
        os.system('python mihota07_japan.py')
    elif choice == "立方":
        a = Decimal(g.enterbox("数字を入力してください："))
        result = a ** Decimal(3)
        g.msgbox("結果は：" + str(result))
        os.system('python mihota07_japan.py')
    elif choice == "立方根":
        a = Decimal(g.enterbox("数字を入力してください："))
        result = a ** (Decimal(1)/Decimal(3))
        g.msgbox("結果は：" + str(result))
        os.system('python mihota07_japan.py')
    elif choice == "終了":
        os.system('python mihota07_japan.py')
    elif choice == "面積":
        choice1 = g.choicebox("幾何学的形状を選択してください：", choices=["円", "三角形", "正方形", "長方形", "台形", '終了'])
        if choice1 == "円":
            a = Decimal(g.enterbox("円の半径を入力してください："))
            result = Decimal(3.14) * a * a
            g.msgbox("円の面積は：" + str(result))
            os.system('python mihota07_japan.py')
        elif choice1 == "三角形":
            a = Decimal(g.enterbox("三角形の底を入力してください："))
            b = Decimal(g.enterbox("三角形の高さを入力してください："))
            result = Decimal(0.5) * a * b
            g.msgbox("三角形の面積は：" + str(result))
            os.system('python mihota07_japan.py')
        elif choice1 == "正方形":
            a = Decimal(g.enterbox("正方形の辺の長さを入力してください："))
            result = a * a
            g.msgbox("正方形の面積は：" + str(result))
            os.system('python mihota07_japan.py')
        elif choice1 == "長方形":
            a = Decimal(g.enterbox("長方形の長さを入力してください："))
            b = Decimal(g.enterbox("長方形の幅を入力してください："))
            result = a * b
            g.msgbox("長方形の面積は：" + str(result))
            os.system('python mihota07_japan.py')
        elif choice1 == "台形":
            a = Decimal(g.enterbox("台形の上底を入力してください："))
            b = Decimal(g.enterbox("台形の下底を入力してください："))
            c = Decimal(g.enterbox("台形の高さを入力してください："))
            result = Decimal(0.5) * (Decimal(a) + Decimal(b)) * Decimal(c)
            g.msgbox("台形の面積は：" + str(result))
            os.system('python mihota07_japan.py')
        elif choice1 == "終了":
            os.system('python mihota07_japan.py')


if __name__ == '__main__':
    main()
