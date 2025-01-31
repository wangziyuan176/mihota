from window import window
import easygui
from tkinter import messagebox

file = easygui.fileopenbox(title='*.mhtfileファイルを選択', filetypes=['mihota専用テキストファイル', '(*.mhtfile)'])
if file:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        easygui.textbox(msg=content, title='ファイル内容', codebox=True)
        window.py_run('mihota07_japan.py')
else:
    messagebox.showinfo(title='ヒント', message='ファイルが選択されていません')
    window.py_run('mihota07_japan.py')
