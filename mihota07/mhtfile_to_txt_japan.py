import easygui
from tkinter import filedialog
from window import window

a = easygui.buttonbox('変換するファイルの種類を選択してください', choices=['mhtfileファイル', 'txtファイル'])

if a == 'mhtfileファイル':
    file = filedialog.askopenfilename(title='変換するファイルを選択してください', filetypes=[('mhtfileファイル', '*.mht')])
    with open('変換後.txt', 'w', encoding='utf-8') as f:
        mht = open(file, 'r', encoding='utf-8')
        cor = mht.read()
        f.write(cor)
        mht.close()
        window.py_run('mihota07_japan.py')

elif a == 'txtファイル':
    file1 = filedialog.askopenfilename(title='変換するファイルを選択してください', filetypes=[('txtファイル', '*.txt')])
    with open('変換後.mhtfile', 'w', encoding='utf-8') as f1:
        mht1 = open(file1, 'r', encoding='utf-8')
        cor1 = mht1.read()
        f1.write(cor1)
        mht1.close()
        window.py_run('mihota07_japan.py')
