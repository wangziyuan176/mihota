import random, easygui
import os
s=int(easygui.enterbox('你要输入这个数字的最小范围:'))
h=int(easygui.enterbox('你要输入这个数字的最大范围:'))
secret = random.randint(s, h)
tries = 0
easygui.msgbox('现在开始猜数字，数字的范围是'+str(s)+'~'+str(h)+'。')
temp = int(easygui.enterbox("请输入一个数字："))
guess = int(temp)

if guess == secret:
    easygui.msgbox("恭喜你一次就猜对了！")
else:
    if guess < secret:
        easygui.msgbox("猜小了!")
    else:
        easygui.msgbox("猜大了！")

while guess != secret and tries < 15:
    temp = int(easygui.enterbox("猜错了，重新猜猜吧:"))
    guess = int(temp)
    tries += 1
    if guess == secret:
        easygui.msgbox("恭喜您，猜对啦！")
    else:
        if guess < secret:
            easygui.msgbox("猜小了！")
        else:
            easygui.msgbox('猜大了')
    while tries >= 30:
        easygui.msgbox("没有机会了")
        break
easygui.msgbox("哈哈，正确数字是" + str(secret))
os.system('python mihota06.py')