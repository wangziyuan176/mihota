import easygui
from tkinter import filedialog
from window import window

# Prompt the user to select the file type to convert
a = easygui.buttonbox('Please select the file type to convert', choices=['mhtfile', 'txt file'])

if a == 'mhtfile':
    # Ask the user to select a mht file
    file = filedialog.askopenfilename(title='Please select the file to convert', filetypes=[('mht file', '*.mht')])
    with open('converted.txt', 'w', encoding='utf-8') as f:
        mht = open(file, 'r', encoding='utf-8')
        cor = mht.read()
        f.write(cor)
        mht.close()
        window.py_run('mihota07_english.py')


elif a == 'txt file':
    # Ask the user to select a txt file
    file1 = filedialog.askopenfilename(title='Please select the file to convert', filetypes=[('txt file', '*.txt')])
    with open('converted.mhtfile', 'w', encoding='utf-8') as f1:
        mht1 = open(file1, 'r', encoding='utf-8')
        cor1 = mht1.read()
        f1.write(cor1)
        mht1.close()
        window.py_run('mihota07_english.py')


