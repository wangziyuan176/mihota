import easygui
from tkinter import messagebox
import time
from window import window
from tqdm.tk import tqdm

easygui.msgbox('Okay, let’s start. Please press OK (I will appear after 25 minutes)')
bar = tqdm(total=1500)
for i in range(0, 1500):
    bar.set_description('Focusing')
    time.sleep(1)
    bar.update(1)
messagebox.showwarning('Reminder', 'Time is up! You can take a 5-minute break!')
bar = tqdm(total=300)
for i in range(0, 300):
    bar.set_description('Taking a break')
    time.sleep(1)
    bar.update(1)
messagebox.showwarning('Reminder', 'A round of Pomodoro is over!')
window.py_run('tomato1_english.py')
