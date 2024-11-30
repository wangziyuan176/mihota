from window import window
import easygui
a=easygui.buttonbox('此电脑','mihota',['设置','猜数字小游戏','输出文件到Windows','番茄钟'])
if a=='设置':
    window.py_run('st.py')
elif a=='输出文件到Windows':
    window.py_run('Windows.py')
elif a=='猜数字小游戏':
    window.py_run('guess_number_game.py')
elif a=='番茄钟':
    window.py_run('tomato1.py')