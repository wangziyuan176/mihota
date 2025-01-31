import easygui
from tkinter import messagebox
import time
from window import window
from tqdm.tk import tqdm
easygui.msgbox('好的，现在开始,请按下OK(25分钟后我会出现)')
bar=tqdm(total=1500)
for i in range(0,1500):
    bar.set_description('专注中')
    time.sleep(1)
    bar.update(1)
messagebox.showwarning('提醒', '时间到!可以休息5分钟了!')
bar=tqdm(total=300)
for i in range(0,300):
    bar.set_description('休息中')
    time.sleep(1)
    bar.update(1)
messagebox.showwarning('提醒','一轮番茄钟结束!')
window.py_run('tomato1.py')