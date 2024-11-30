import easygui
from window import window

a=easygui.choicebox('设置','mihota',['时间','关于','返回'])
if a=='时间':
    window.py_run('st1.py')
elif a=='关于':
    window.py_run('st2.py')
elif a=='返回':
    window.py_run('mihota02.py')