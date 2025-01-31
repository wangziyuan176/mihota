import random, easygui
import os

s = int(easygui.enterbox('この数字の最小範囲を入力してください:'))
h = int(easygui.enterbox('この数字の最大範囲を入力してください:'))
secret = random.randint(s, h)
tries = 0
easygui.msgbox('これから数字を当てるゲームを開始します、数字の範囲は' + str(s) + '〜' + str(h) + 'です。')
temp = int(easygui.enterbox("数字を入力してください："))
guess = int(temp)

if guess == secret:
    easygui.msgbox("おめでとうございます、一発で当たりました！")
else:
    if guess < secret:
        easygui.msgbox("小さすぎます！")
    else:
        easygui.msgbox("大きすぎます！")

while guess != secret and tries < 15:
    temp = int(easygui.enterbox("間違えました、もう一度試してみてください:"))
    guess = int(temp)
    tries += 1
    if guess == secret:
        easygui.msgbox("おめでとうございます、当たりました！")
    else:
        if guess < secret:
            easygui.msgbox("小さすぎます！")
        else:
            easygui.msgbox('大きすぎます')
    if tries >= 30:
        easygui.msgbox("チャンスはもうありません")
        break

easygui.msgbox("ハハ、正しい数字は" + str(secret) + "です")
os.system('python mihota07_japan.py')
