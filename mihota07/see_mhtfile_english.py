from window import window
import easygui
from tkinter import messagebox

file = easygui.fileopenbox(title='Choose a *.mhtfile file', filetypes=['mihota special text file', '(*.mhtfile)'])
if file:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        easygui.textbox(msg=content, title='File Content', codebox=True)
        window.py_run('mihota07_english.py')
else:
    messagebox.showinfo(title='Prompt', message='No file selected')
    window.py_run('mihota07_english.py')
