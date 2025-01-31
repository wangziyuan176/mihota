import random, easygui
import os

s = int(easygui.enterbox('Please enter the minimum range for the number:'))
h = int(easygui.enterbox('Please enter the maximum range for the number:'))
secret = random.randint(s, h)
tries = 0
easygui.msgbox('Now let\'s start guessing the number, the range is ' + str(s) + ' to ' + str(h) + '.')
temp = int(easygui.enterbox("Please enter a number:"))
guess = int(temp)

if guess == secret:
    easygui.msgbox("Congratulations! You guessed it right on the first try!")
else:
    if guess < secret:
        easygui.msgbox("Too low!")
    else:
        easygui.msgbox("Too high!")

while guess != secret and tries < 15:
    temp = int(easygui.enterbox("Wrong guess, try again:"))
    guess = int(temp)
    tries += 1
    if guess == secret:
        easygui.msgbox("Congratulations! You guessed it right!")
    else:
        if guess < secret:
            easygui.msgbox("Too low!")
        else:
            easygui.msgbox("Too high!")

    while tries >= 30:
        easygui.msgbox("No more chances left.")
        break

easygui.msgbox("Ha ha, the correct number is " + str(secret))
os.system('python mihota06_english.py')

