import easygui
from window import window
from tkinter import filedialog
a=easygui.buttonbox('请选择要转换的文件类型',choices=['mhtfile文件','txt文件'])
if a=='mhtfile文件':
    file=filedialog.askopenfilename(title='请选择要转换的文件文件',filetypes=[('mhtfile文件','*.mht')])
    with open('转换后.txt','w',encoding='utf-8') as f:
        mht=open(file, 'r', encoding='utf-8')
        cor = mht.read()
        f.write(cor)
        mht.close()


elif a=='txt文件':
    file1=filedialog.askopenfilename(title='请选择要转换的文件文件', filetypes=[('txt文件', '*.txt')])
    with open('转换后.mhtfile', 'w', encoding='utf-8') as f1:
        mht1=open(file1, 'r', encoding='utf-8')
        cor1=mht1.read()
        f1.write(cor1)
        mht1.close()




