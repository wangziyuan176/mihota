import easygui
from window import window
a=easygui.buttonbox('番茄钟(专注25分钟，休息5分钟)','番茄钟',['开始','退出'])
if a=='退出':
    window.py_run('mihota04.py')
elif a=='开始':
    window.py_run('tomato.py')