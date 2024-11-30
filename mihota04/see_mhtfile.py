from window import window
import easygui
from tkinter import messagebox
file=easygui.fileopenbox(title='选择一个*.mhtfile文件',filetypes=['mihota专用文本文件','(*.mhtfile)'])
if file:
    with open(file,'r',encoding='utf-8') as f:
        content=f.read()
        easygui.textbox(msg=content, title='文件内容',codebox=True)
        window.py_run('mihota04.py')
else:
    messagebox.showinfo(title='提示', message='未选择文件')
    window.py_run('mihota04.py')