import easygui
from tkinter import messagebox
import time
from window import window
from tqdm.tk import tqdm

easygui.msgbox('了解しました、これから開始します。OKを押してください（25分後に表示されます）')
bar = tqdm(total=1500)
for i in range(0, 1500):
    bar.set_description('集中中')
    time.sleep(1)
    bar.update(1)
messagebox.showwarning('リマインダー', '時間です！5分間休憩してください！')
bar = tqdm(total=300)
for i in range(0, 300):
    bar.set_description('休憩中')
    time.sleep(1)
    bar.update(1)
messagebox.showwarning('リマインダー', '1回のポモドーロが終了しました！')
window.py_run('tomato1_japan.py')
