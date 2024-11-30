import easygui
from window import window
a=easygui.buttonbox('电脑',choices=['设置','输出文件到Windows'])
if a=='设置':
    window.py_run('st.py')
elif a=='输出文件到Windows':
    window.py_run('Windows.py')
